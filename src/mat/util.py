from datetime import datetime
from pathlib import Path
from typing import List, Union

def find_files(folder_path: Union[str, Path], extension: str = "*.xlsx", recursive: bool = False) -> List[Path]:
    """
    Searches for files with a specified extension within a given folder.  Can search recursively.

    Args:
        folder_path: The path to the folder to search (string or Path object).
        extension: The file extension pattern to search for (e.g., "*.xlsx", "*.csv", "*.txt"). 
                   Defaults to "*.xlsx". Use "*" to find all files.
        recursive: If True, searches subfolders recursively. Defaults to False.

    Returns:
        A list of Path objects representing the found files. Returns an empty list if no files 
        are found, the folder doesn't exist, or if there's an error accessing the folder.

    Raises:
        TypeError: if folder_path is not a string or Path object.
        ValueError: if extension is not a valid glob pattern.
    """
    if not isinstance(folder_path, (str, Path)):
        raise TypeError("folder_path must be a string or Path object.")

    folder = Path(folder_path)

    if not folder.is_dir():
        print(f"Error: '{folder_path}' is not a valid directory.")
        return []

    try:
        if recursive:
            files = list(folder.rglob(extension)) #Use rglob for recursive search
        else:
            files = list(folder.glob(extension))
        return files
    except OSError as e:
        print(f"Error accessing folder '{folder_path}': {e}")
        return []
    except ValueError as e:
        print(f"Invalid glob pattern: {e}")
        return []