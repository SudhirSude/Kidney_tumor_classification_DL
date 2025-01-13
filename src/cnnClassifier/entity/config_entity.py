from dataclasses import dataclass
from pathlib import Path

# @dataclass decorator, which automatically adds special methods like __init__, __repr__, and __eq__ to a class.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path