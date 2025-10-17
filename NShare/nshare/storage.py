"""Storage abstractions for reading and writing files."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .utils import format_size, iter_directory, resolve_path


@dataclass
class FileMeta:
    name: str
    path: Path
    is_dir: bool
    size: int
    size_display: str
    modified_ts: float


class Storage:
    def __init__(self, root: Path, hide_hidden: bool = True) -> None:
        self.root = root
        self.hide_hidden = hide_hidden

    def list(self, relative: Path | None = None) -> Iterable[FileMeta]:
        target = self.root if relative is None else resolve_path(self.root, relative)
        for entry in iter_directory(target, hide_hidden=self.hide_hidden):
            stat = entry.stat()
            yield FileMeta(
                name=entry.name,
                path=entry.relative_to(self.root),
                is_dir=entry.is_dir(),
                size=stat.st_size,
                size_display=format_size(stat.st_size),
                modified_ts=stat.st_mtime,
            )

    def exists(self, relative: Path) -> bool:
        try:
            path = resolve_path(self.root, relative)
        except ValueError:
            return False
        return path.exists()

    def open_file(self, relative: Path) -> Path:
        path = resolve_path(self.root, relative)
        if not path.exists() or not path.is_file():
            raise FileNotFoundError(relative)
        return path

    def make_directory(self, relative: Path) -> Path:
        path = resolve_path(self.root, relative)
        path.mkdir(parents=True, exist_ok=True)
        return path

    def save_file(self, relative: Path, source_path: Path) -> Path:
        dest = resolve_path(self.root, relative)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, dest)
        return dest

    def save_bytes(self, relative: Path, data: bytes) -> Path:
        dest = resolve_path(self.root, relative)
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open("wb") as fh:
            fh.write(data)
        return dest

    def remove(self, relative: Path) -> None:
        path = resolve_path(self.root, relative)
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink(missing_ok=True)
