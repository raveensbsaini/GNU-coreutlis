import os
import sys

from pathlib import Path

def get_binary_path(binary_name: str) -> Path | None:
    paths = os.environ["PATH"]
    for path in paths.split(":"):
        path = Path(path)
        if (path/binary_name).is_file():
            return path/binary_name

if __name__ == "__main__":
    print(str(get_binary_path(sys.argv[1])))
        
