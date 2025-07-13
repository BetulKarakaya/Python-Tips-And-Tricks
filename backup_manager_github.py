from shutil import copy2
from pathlib import Path
from datetime import datetime

class BackupManager:
    def __init__(self, source_file, backup_folder="backups"):
        self.source = Path(source_file)
        self.backup_dir = Path(backup_folder)
        self.backup_dir.mkdir(exist_ok=True)

    def backup(self):
        if not self.source.exists():
            print("Source file does not exist.")
            return
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{self.source.stem}_{timestamp}{self.source.suffix}"
        destination = self.backup_dir / backup_name
        copy2(self.source, destination)
        print(f"Backup created: {destination}")

def main():
    file_to_backup = "important_notes.txt"
    manager = BackupManager(file_to_backup)
    manager.backup()

if __name__ == "__main__":
    main()