import atexit
from pathlib import Path
import os

class TempFileManager:
    """Automatically creates and deletes a temporary file in the script directory using atexit."""

    def __init__(self):
        # Get the directory where this script is located
        self.base_dir = Path(__file__).parent.resolve()
        self.file_path = self.base_dir / "temp_session.txt"

        # Create the file
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write("=== Temporary Session File ===\n")

        print(f"-- Temporary file created at: {self.file_path}")

        # Register cleanup function to delete the file when program exits
        atexit.register(self.cleanup)

    def write_data(self, data: str):
        """Write data into the temporary file."""
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(f"{data}\n")
        print(f"- Data written: {data}")

    def cleanup(self):
        """Delete the temporary file automatically on exit."""
        if self.file_path.exists():
            os.remove(self.file_path)
            print(f"- Temporary file deleted automatically: {self.file_path}")
        else:
            print("⚠️ File already deleted or missing.")

def main():
    manager = TempFileManager()
    manager.write_data("Running analysis...")
    manager.write_data("Logging progress...")
    print("Program finished. File will be deleted on exit.")

if __name__ == "__main__":
    main()
