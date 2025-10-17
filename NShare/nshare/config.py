"""Configuration utilities for NShare."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional

import os


ENV_FILE_NAME = ".env"


def _parse_bool(value: Optional[str], default: bool = False) -> bool:
    if value is None:
        return default
    value = value.strip().lower()
    if value in {"1", "true", "yes", "on"}:
        return True
    if value in {"0", "false", "no", "off"}:
        return False
    return default


def _parse_int(value: Optional[str], default: int) -> int:
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _parse_list(value: Optional[str]) -> Iterable[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def _load_env_file(base_path: Path) -> dict[str, str]:
    env_path = base_path / ENV_FILE_NAME
    if not env_path.exists():
        return {}
    data: dict[str, str] = {}
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, raw_value = line.partition("=")
        data[key.strip()] = raw_value.strip()
    return data


@dataclass
class Config:
    """Resolved configuration for the server."""

    port: int = 8000
    root_path: Path = field(default_factory=lambda: Path.cwd())
    allow_upload: bool = True
    max_upload_size: int = 100 * 1024 * 1024  # 100 MB
    auth_token: Optional[str] = None
    hide_hidden: bool = True
    allowed_extensions: Optional[set[str]] = None
    host: str = "0.0.0.0"

    @property
    def max_upload_size_mb(self) -> float:
        return self.max_upload_size / (1024 * 1024)


def load_config(
    root: Optional[str] = None,
    port: Optional[int] = None,
    allow_upload: Optional[bool] = None,
    max_upload_size: Optional[int] = None,
    auth_token: Optional[str] = None,
    hide_hidden: Optional[bool] = None,
    allowed_extensions: Optional[Iterable[str]] = None,
    host: Optional[str] = None,
) -> Config:
    """Create a Config instance from parameters, .env, and environment variables."""

    base_path = Path.cwd()
    env_overrides = {**_load_env_file(base_path), **os.environ}

    resolved_root = root or env_overrides.get("NSHARE_ROOT")
    resolved_port = port or _parse_int(env_overrides.get("NSHARE_PORT"), 8000)
    resolved_allow_upload = (
        allow_upload
        if allow_upload is not None
        else _parse_bool(env_overrides.get("NSHARE_ALLOW_UPLOAD"), True)
    )
    resolved_max_upload_size = (
        max_upload_size
        if max_upload_size is not None
        else _parse_int(env_overrides.get("NSHARE_MAX_UPLOAD"), 100 * 1024 * 1024)
    )
    resolved_token = auth_token or env_overrides.get("NSHARE_AUTH_TOKEN")
    resolved_hide_hidden = (
        hide_hidden
        if hide_hidden is not None
        else _parse_bool(env_overrides.get("NSHARE_HIDE_HIDDEN"), True)
    )
    resolved_allowed = allowed_extensions or _parse_list(
        env_overrides.get("NSHARE_ALLOWED_EXTENSIONS")
    )
    resolved_host = host or env_overrides.get("NSHARE_HOST") or "0.0.0.0"

    config = Config()
    config.port = resolved_port
    config.root_path = Path(resolved_root).expanduser().resolve() if resolved_root else Path.cwd()
    config.allow_upload = resolved_allow_upload
    config.max_upload_size = resolved_max_upload_size
    config.auth_token = resolved_token
    config.hide_hidden = resolved_hide_hidden
    if resolved_allowed:
        config.allowed_extensions = {ext.lower().lstrip(".") for ext in resolved_allowed}
    else:
        config.allowed_extensions = None

    config.host = resolved_host
    return config
