from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileItem:
    name: str
    path: Path
    link: str
    description: str
    is_dir: bool