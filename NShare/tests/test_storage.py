from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from nshare.storage import Storage


class StorageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.storage = Storage(self.root)

    def tearDown(self) -> None:  # noqa: D401
        self.tempdir.cleanup()

    def test_save_and_open_file(self) -> None:
        data = b"hello"
        dest = Path("foo.txt")
        self.storage.save_bytes(dest, data)
        opened = self.storage.open_file(dest)
        self.assertEqual(opened.read_text(), "hello")

    def test_disallow_escape(self) -> None:
        with self.assertRaises(ValueError):
            self.storage.open_file(Path("../evil"))


if __name__ == "__main__":
    unittest.main()
