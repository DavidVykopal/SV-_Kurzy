"""Utility helpers for NShare."""

from __future__ import annotations

import ipaddress
import logging
import socket
from pathlib import Path
from typing import Iterable, Optional


def configure_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )


def resolve_path(root: Path, target: Path) -> Path:
    resolved = (root / target).resolve()
    if not str(resolved).startswith(str(root.resolve())):
        raise ValueError("Path outside of root is not allowed")
    return resolved


def iter_directory(path: Path, hide_hidden: bool = True) -> Iterable[Path]:
    for entry in sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower())):
        if hide_hidden and entry.name.startswith('.'):
            continue
        yield entry


def format_size(num_bytes: int) -> str:
    step = 1024
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(num_bytes)
    for unit in units:
        if size < step or unit == units[-1]:
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} {unit}"
        size /= step
    return f"{size:.1f} TB"


def get_lan_ip() -> str:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        ipaddress.ip_address(ip)
        return ip
    except Exception:
        return "127.0.0.1"


def sanitize_filename(name: str) -> Optional[str]:
    candidate = Path(name).name
    if candidate in {"", ".", ".."}:
        return None
    return candidate
