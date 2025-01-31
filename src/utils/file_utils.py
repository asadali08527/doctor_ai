import os

def ensure_directory_exists(file_path: str) -> None:
    """Ensure the directory for the given file path exists."""
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)