import os
import shutil
from pathlib import Path
from datetime import datetime

class ImageOrganizer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def organize_by_date(self):
        """Splits images into subfolders based on creation date"""
        for file in self.folder_path.iterdir():
            if file.is_file() and file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                creation_time = datetime.fromtimestamp(file.stat().st_mtime)
                date_folder = self.folder_path / creation_time.strftime('%Y-%m-%d')

                # Create the date folder
                date_folder.mkdir(exist_ok=True)

                # Move file
                shutil.move(str(file), str(date_folder / file.name))
                print(f"Moved: {file.name} → {date_folder}")

def main():
    path = input("Enter the folder path: ")
    organizer = ImageOrganizer(path)
    organizer.organize_by_date()


if __name__ == "__main__":
    main()
