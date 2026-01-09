import unittest
from pathlib import Path
import tempfile

from enlist_io import scan_directory
from enlist_io.models import FileItem


class TestScanDirectory(unittest.TestCase):

    def test_returns_list(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = scan_directory(tmp)
            self.assertIsInstance(result, list)

    def test_accepts_path_object(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            result = scan_directory(path)
            self.assertIsInstance(result, list)

    def test_detects_files_and_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)

            file = tmp_path / "file.txt"
            file.write_text("hello")

            folder = tmp_path / "folder"
            folder.mkdir()

            items = scan_directory(tmp_path)

            self.assertEqual(len(items), 2)

            for item in items:
                self.assertIsInstance(item, FileItem)
                self.assertIsInstance(item.is_dir, bool)
                self.assertTrue(item.name in {"file.txt", "folder"})

    def test_invalid_path_raises_error(self):
        with self.assertRaises(FileNotFoundError):
            scan_directory("this/path/does/not/exist")