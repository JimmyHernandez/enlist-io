import unittest
from pathlib import Path
import tempfile
import csv

from enlist_io import scan_directory, export_to_csv


class TestExportToCSV(unittest.TestCase):

    def test_creates_csv_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)

            file = tmp_path / "file.txt"
            file.write_text("hello")

            items = scan_directory(tmp_path)

            output_csv = tmp_path / "output.csv"
            export_to_csv(items, output_csv)

            self.assertTrue(output_csv.exists())

    def test_csv_has_header_and_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)

            file = tmp_path / "file.txt"
            file.write_text("hello")

            items = scan_directory(tmp_path)

            output_csv = tmp_path / "output.csv"
            export_to_csv(items, output_csv)

            with open(output_csv, newline="", encoding="utf-8") as f:
                reader = list(csv.reader(f))

            self.assertGreaterEqual(len(reader), 2)
            self.assertEqual(
                reader[0],
                ["Name", "Path", "Link", "Description", "IsDir"]
            )
