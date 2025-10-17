"""Launch NShare server with optional Ngrok tunnel."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

from nshare.config import load_config
from nshare.server import run_server
from nshare.utils import configure_logging


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run NShare and expose via Ngrok")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Root directory to share")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address")
    parser.add_argument("--ngrok-path", type=Path, default=Path(__file__).resolve().parent.parent / "ngrok" / "ngrok", help="Path to ngrok binary")
    parser.add_argument("--no-upload", action="store_true", help="Disable file uploads")
    parser.add_argument("--max-upload", type=int, default=100 * 1024 * 1024, help="Max upload size in bytes")
    parser.add_argument("--auth-token", type=str, help="Require token for access")
    parser.add_argument("--show-hidden", action="store_true", help="Expose hidden files")
    parser.add_argument("--allowed-extensions", type=str, help="Comma-separated list of allowed upload extensions")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    parser.add_argument("--ngrok-config", type=Path, help="Path to ngrok configuration file")
    return parser.parse_args(argv)


def start_ngrok(binary: Path, port: int, config_path: Path | None = None) -> subprocess.Popen:
    cmd = [str(binary), "http", str(port)]
    if config_path and config_path.exists():
        cmd.extend(["--config", str(config_path)])
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    configure_logging(verbose=args.verbose)

    allowed_exts = None
    if args.allowed_extensions:
        allowed_exts = [ext.strip() for ext in args.allowed_extensions.split(",") if ext.strip()]

    conf = load_config(
        root=str(args.root.resolve()),
        port=args.port,
        allow_upload=not args.no_upload,
        max_upload_size=args.max_upload,
        auth_token=args.auth_token,
        hide_hidden=not args.show_hidden,
        allowed_extensions=allowed_exts,
        host=args.host,
    )

    thread, server = run_server(conf)

    ngrok_binary = args.ngrok_path
    if ngrok_binary.is_dir():
        ngrok_binary = ngrok_binary / "ngrok"
    if not ngrok_binary.exists():
        print(f"Ngrok binary not found at {ngrok_binary}. Server running locally only.")
        try:
            thread.join()
        except KeyboardInterrupt:
            server.shutdown()
        return 0

    process = start_ngrok(ngrok_binary, conf.port, args.ngrok_config)
    try:
        print("Ngrok started. Logs:")
        while True:
            if process.poll() is not None:
                print("Ngrok process terminated.")
                break
            line = process.stdout.readline()
            if not line:
                time.sleep(0.1)
                continue
            print(line.decode("utf-8", errors="ignore"), end="")
    except KeyboardInterrupt:
        process.terminate()
        server.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
