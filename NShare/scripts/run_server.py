"""CLI entry point for running NShare server."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from nshare import config
from nshare.server import run_server
from nshare.utils import configure_logging


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run NShare local file sharing server")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Root directory to share")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on (read-write)")
    parser.add_argument("--readonly-port", type=int, help="Additional read-only port")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address")
    parser.add_argument("--no-upload", action="store_true", help="Disable file uploads")
    parser.add_argument("--max-upload", type=int, default=100 * 1024 * 1024, help="Max upload size in bytes")
    parser.add_argument("--auth-token", type=str, help="Require token for access")
    parser.add_argument("--show-hidden", action="store_true", help="Expose hidden files")
    parser.add_argument("--allowed-extensions", type=str, help="Comma-separated list of allowed upload extensions")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    configure_logging(verbose=args.verbose)

    allowed_exts = None
    if args.allowed_extensions:
        allowed_exts = [ext.strip() for ext in args.allowed_extensions.split(",") if ext.strip()]

    conf = config.load_config(
        root=str(args.root.resolve()),
        port=args.port,
        allow_upload=not args.no_upload,
        max_upload_size=args.max_upload,
        auth_token=args.auth_token,
        hide_hidden=not args.show_hidden,
        allowed_extensions=allowed_exts,
        host=args.host,
    )

    threads, servers = run_server(conf, readonly_port=args.readonly_port)
    try:
        # Wait for all threads
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        # Shutdown all servers
        for server in servers:
            server.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
