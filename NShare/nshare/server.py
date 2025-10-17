"""HTTP server implementation for NShare."""

from __future__ import annotations

import io
import json
import logging
import mimetypes
import threading
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler
from pathlib import Path
from shutil import copyfileobj
from typing import Optional
from urllib.parse import parse_qs, unquote, urlparse
from email.message import EmailMessage

from .config import Config
from .security import require_token
from .storage import Storage
from .utils import get_lan_ip, sanitize_filename
from . import views


class NShareRequestHandler(SimpleHTTPRequestHandler):
    server_version = "NShare/1.0"

    def __init__(self, *args, **kwargs):
        self.config: Config = kwargs.pop("config")
        self.is_readonly: bool = kwargs.pop("is_readonly", False)
        self.storage = Storage(self.config.root_path, hide_hidden=self.config.hide_hidden)
        self.static_root = (Path(__file__).resolve().parent / "static").resolve()
        super().__init__(*args, directory=str(self.config.root_path), **kwargs)

    def translate_path(self, path: str) -> str:
        original = Path(url_to_path(path))
        try:
            resolved = self.storage.open_file(original)
        except FileNotFoundError:
            return super().translate_path(path)
        return str(resolved)

    def log_message(self, format: str, *args) -> None:
        logging.info("%s - %s", self.address_string(), format % args)

    def get_token_from_request(self) -> Optional[str]:
        return self._query_params().get("token")

    def _send_html(self, body: str, status: HTTPStatus = HTTPStatus.OK) -> None:
        body_bytes = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body_bytes)))
        self.end_headers()
        self.wfile.write(body_bytes)

    @require_token(lambda self: self.config.auth_token)
    def do_GET(self):
        target = Path(url_to_path(self._query_params().get("path", "")))

        if self.path.startswith("/static/"):
            return self._serve_static()

        if self.path.startswith("/api/notice"):
            return self._handle_api_notice()

        if self.path.startswith("/api/list"):
            return self._handle_api_list(target)

        if self.path.startswith("/download"):
            return self._handle_download(target)

        if self.path.startswith("/upload") and self.command == "GET":
            if not self.config.allow_upload or self.is_readonly:
                self.send_error(HTTPStatus.FORBIDDEN, "Uploads disabled")
                return
            body = views.render_upload_form(target)
            self._send_html(body)
            return

        try:
            items = list(self.storage.list(target))
        except (FileNotFoundError, ValueError):
            self.send_error(HTTPStatus.NOT_FOUND, "Path not found")
            return

        # Show upload button only if uploads are allowed and not read-only
        allow_upload_display = self.config.allow_upload and not self.is_readonly
        body = views.render_index(
            target,
            items,
            allow_upload_display,
            self.config.auth_token is not None,
            get_notice_board(),
            not self.is_readonly
        )
        self._send_html(body)

    @require_token(lambda self: self.config.auth_token)
    def do_DELETE(self):
        """Handle DELETE requests for file/folder deletion."""
        if self.is_readonly:
            self.send_error(HTTPStatus.FORBIDDEN, "Read-only mode")
            return

        if not self.path.startswith("/api/delete"):
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        target = Path(url_to_path(self._query_params().get("path", "")))
        if not target or target == Path("."):
            self.send_error(HTTPStatus.BAD_REQUEST, "Invalid path")
            return

        try:
            if not self.storage.exists(target):
                self.send_error(HTTPStatus.NOT_FOUND, "File not found")
                return

            self.storage.remove(target)
            response = {"success": True, "path": str(target)}
            response_body = json.dumps(response).encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response_body)))
            self.end_headers()
            self.wfile.write(response_body)
        except Exception as e:
            logging.error(f"Error deleting file: {e}")
            self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR, "Delete failed")

    @require_token(lambda self: self.config.auth_token)
    def do_POST(self):
        # Handle notice board updates (only for write port)
        if self.path.startswith("/api/notice"):
            if self.is_readonly:
                self.send_error(HTTPStatus.FORBIDDEN, "Read-only mode")
                return
            return self._handle_api_notice_update()

        if not self.config.allow_upload or self.is_readonly:
            self.send_error(HTTPStatus.FORBIDDEN, "Uploads disabled")
            return

        if not self.path.startswith("/upload"):
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        content_type = self.headers.get("Content-Type")
        if not content_type:
            self.send_error(HTTPStatus.BAD_REQUEST, "Missing Content-Type")
            return

        # Parse Content-Type header using email.message
        msg = EmailMessage()
        msg['content-type'] = content_type
        ctype = msg.get_content_type()

        if ctype != "multipart/form-data":
            self.send_error(HTTPStatus.BAD_REQUEST, "Unsupported Content-Type")
            return

        boundary = msg.get_param('boundary')
        if not boundary:
            self.send_error(HTTPStatus.BAD_REQUEST, "Missing multipart boundary")
            return

        target = Path(self._query_params().get("target", ""))
        saved_files = []
        total_size = 0

        for headers, content in parse_multipart(self.rfile, boundary.encode(), self.headers):
            disposition = headers.get("Content-Disposition", "")
            if "filename=" not in disposition:
                if "name=\"target\"" in disposition:
                    target_str = content.decode("utf-8", errors="ignore").strip()
                    target = Path(target_str)
                continue
            filename = extract_filename(disposition)
            if not filename:
                continue
            sanitized = sanitize_filename(filename)
            if not sanitized:
                continue
            if self.config.allowed_extensions is not None:
                ext = Path(sanitized).suffix.lower().lstrip(".")
                if ext not in self.config.allowed_extensions:
                    continue
            data = content
            total_size += len(data)
            if total_size > self.config.max_upload_size:
                self.send_error(HTTPStatus.REQUEST_ENTITY_TOO_LARGE, "Upload too large")
                return
            saved_files.append((target / sanitized, io.BytesIO(data)))

        for relative, buffer in saved_files:
            temp_file = self.config.root_path / ".__upload.tmp"
            with temp_file.open("wb") as fh:
                fh.write(buffer.getvalue())
            self.storage.save_file(relative, temp_file)
            temp_file.unlink(missing_ok=True)

        self.send_response(HTTPStatus.SEE_OTHER)
        redirect = target.as_posix()
        self.send_header("Location", f"/?path={redirect}" if redirect else "/")
        self.end_headers()

    def _handle_download(self, target: Path):
        try:
            path = self.storage.open_file(target)
        except FileNotFoundError:
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return

        mime_type, _ = mimetypes.guess_type(str(path))
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", mime_type or "application/octet-stream")
        self.send_header("Content-Disposition", f"attachment; filename=\"{path.name}\"")
        self.send_header("Content-Length", str(path.stat().st_size))
        self.end_headers()
        with path.open("rb") as file_obj:
            copyfileobj(file_obj, self.wfile)

    def _handle_api_list(self, target: Path):
        try:
            items = list(self.storage.list(target))
        except (FileNotFoundError, ValueError):
            self.send_error(HTTPStatus.NOT_FOUND, "Path not found")
            return

        payload = {
            "path": target.as_posix(),
            "items": [
                {
                    "name": item.name,
                    "path": item.path.as_posix(),
                    "isDir": item.is_dir,
                    "size": item.size,
                    "sizeDisplay": item.size_display,
                }
                for item in items
            ],
        }

        body = json.dumps(payload).encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _handle_api_notice(self):
        """Handle GET request for notice board content."""
        payload = {"text": get_notice_board()}
        body = json.dumps(payload).encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _handle_api_notice_update(self):
        """Handle POST request to update notice board content."""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))
            text = data.get('text', '')
            set_notice_board(text)

            response = {"success": True, "text": text}
            response_body = json.dumps(response).encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response_body)))
            self.end_headers()
            self.wfile.write(response_body)
        except Exception as e:
            logging.error(f"Error updating notice board: {e}")
            self.send_error(HTTPStatus.BAD_REQUEST, "Invalid request")
    def _serve_static(self):
        relative = url_to_path(self.path[len("/static/"):])
        file_path = (self.static_root / relative).resolve()
        if not str(file_path).startswith(str(self.static_root)) or not file_path.exists():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        mime_type, _ = mimetypes.guess_type(str(file_path))
        data = file_path.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", mime_type or "application/octet-stream")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _query_params(self) -> dict[str, str]:
        parsed = urlparse(self.path)
        return {k: v[0] for k, v in parse_qs(parsed.query, keep_blank_values=True).items() if v}


def run_server(config: Config, readonly_port: Optional[int] = None):
    """Start the NShare server.

    Args:
        config: Server configuration
        readonly_port: If provided, start a second read-only server on this port

    Returns:
        tuple: (threads, servers) - list of threads and HTTPServer instances
    """
    from http.server import ThreadingHTTPServer

    threads = []
    servers = []
    lan_ip = get_lan_ip()

    # Start main read-write server
    def handler_rw(*args, **kwargs):
        return NShareRequestHandler(*args, config=config, is_readonly=False, **kwargs)

    server_address = (config.host, config.port)
    httpd = ThreadingHTTPServer(server_address, handler_rw)

    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    threads.append(thread)
    servers.append(httpd)

    logging.info(
        "Serving (READ-WRITE) on http://%s:%s (LAN: http://%s:%s)",
        config.host,
        config.port,
        lan_ip,
        config.port,
    )

    # Start read-only server if requested
    if readonly_port:
        def handler_ro(*args, **kwargs):
            return NShareRequestHandler(*args, config=config, is_readonly=True, **kwargs)

        readonly_address = (config.host, readonly_port)
        httpd_ro = ThreadingHTTPServer(readonly_address, handler_ro)

        thread_ro = threading.Thread(target=httpd_ro.serve_forever, daemon=True)
        thread_ro.start()
        threads.append(thread_ro)
        servers.append(httpd_ro)

        logging.info(
            "Serving (READ-ONLY) on http://%s:%s (LAN: http://%s:%s)",
            config.host,
            readonly_port,
            lan_ip,
            readonly_port,
        )

    return threads, servers


def url_to_path(value: str) -> str:
    return unquote(value).lstrip("/")


def parse_multipart(rfile, boundary: bytes, headers):
    """Parse multipart form data."""
    import email.parser
    from io import BytesIO

    # Read content length
    content_length = int(headers.get('Content-Length', 0))
    if content_length <= 0:
        return

    # Read all data
    data = rfile.read(content_length)

    # Split by boundary
    parts = data.split(b'--' + boundary)

    for part in parts[1:-1]:  # Skip first empty and last closing
        if not part or part == b'--\r\n' or part == b'\r\n':
            continue

        # Split headers and content
        if b'\r\n\r\n' in part:
            header_data, content = part.split(b'\r\n\r\n', 1)
        else:
            continue

        # Remove trailing \r\n from content
        content = content.rstrip(b'\r\n')

        # Parse headers
        header_text = header_data.decode('utf-8', errors='ignore')
        parsed_headers = {}
        for line in header_text.split('\r\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                parsed_headers[key.strip()] = value.strip()

        yield parsed_headers, content


def extract_filename(disposition: str) -> Optional[str]:
    """Extract filename from Content-Disposition header."""
    import re

    # Try filename*= first (RFC 5987)
    match = re.search(r"filename\*=(?:UTF-8''|utf-8'')(.+?)(?:;|$)", disposition)
    if match:
        from urllib.parse import unquote
        return unquote(match.group(1))

    # Try standard filename=
    match = re.search(r'filename="?([^"]+)"?', disposition)
    if match:
        return match.group(1)

    return None


# Global notice board storage with file persistence
_notice_board_lock = threading.Lock()
_notice_board_file = Path.home() / ".nshare_data" / "notice_board.txt"


def get_notice_board() -> str:
    """Get the current notice board text from file."""
    with _notice_board_lock:
        try:
            if _notice_board_file.exists():
                return _notice_board_file.read_text(encoding="utf-8")
            return ""
        except Exception as e:
            logging.error(f"Error reading notice board: {e}")
            return ""


def set_notice_board(text: str) -> None:
    """Set the notice board text and save to file."""
    with _notice_board_lock:
        try:
            _notice_board_file.parent.mkdir(parents=True, exist_ok=True)
            _notice_board_file.write_text(text, encoding="utf-8")
        except Exception as e:
            logging.error(f"Error saving notice board: {e}")


