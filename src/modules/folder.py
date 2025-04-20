import os
from pathlib import Path


class Folder:
    """
    A class to manage folders for the project.
    """

    def __init__(self, folder: str) -> None:
        """
        Initialize the Folder class.

        Args:
            folder (str): The path to the root folder to be managed.
        """
        self._folder: str = folder
        self.extracted_files: list[str] = []

    def get_files(self, folder_path: str | None = None) -> list[str]:
        """
        Recursively get .txt files and extract month names from filenames.

        Args:
            folder_path (str, optional): The current folder to scan. Defaults to the root folder.

        Returns:
            list[str]: A list of extracted month names from .txt files.
        """
        if folder_path is None:
            folder_path = self._folder

        for item in os.listdir(folder_path):
            full_path = os.path.join(folder_path, item)

            if os.path.isdir(full_path):
                # Recursively explore subdirectories
                self.get_files(full_path)

            elif item.endswith(".txt"):
                # Extract month name from filename
                month_name = item.split()[-1].replace(".txt", "")
                self.extracted_files.append(month_name)

        return self.extracted_files
