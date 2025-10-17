from __future__ import annotations

import unittest
from pathlib import Path

from nshare.utils import sanitize_filename, resolve_path


class UtilsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path("/tmp/test_root").resolve()

    def test_sanitize_filename(self) -> None:
        self.assertEqual(sanitize_filename("foo.txt"), "foo.txt")
        self.assertEqual(sanitize_filename("../foo.txt"), "foo.txt")
        self.assertIsNone(sanitize_filename(".."))

    def test_resolve_path_disallows_escape(self) -> None:
        with self.assertRaises(ValueError):
            resolve_path(self.root, Path("../escape"))


if __name__ == "__main__":
    unittest.main()
