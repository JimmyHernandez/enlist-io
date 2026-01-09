from pathlib import Path
from .models import FileItem
import csv


def scan_directory(folder: str | Path) -> list[FileItem]:
    folder = Path(folder)
    if not folder.exists():
        raise FileNotFoundError(f"{folder} does not exist")

    items: list[FileItem] = []

    for item in folder.iterdir():
        description = "Directorio" if item.is_dir() else f"Archivo                  {item.suffix or 'sin extensión'}"
        link = item.resolve().as_uri()
        items.append(FileItem(name=item.name, path=item, link=link,                 description=description, is_dir=item.is_dir()))

    return items


def export_to_csv(items: list[FileItem], output_file: str) -> None:
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Path", "Link", "Description", "IsDir"])
        for item in items:
            writer.writerow([item.name, str(item.path), item.link,                      item.description, item.is_dir])