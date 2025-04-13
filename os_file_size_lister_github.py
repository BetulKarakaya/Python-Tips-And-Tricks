import os

class FileScanner:
    def __init__(self, root_dir, extension_filter=None):
        self.root_dir = root_dir
        self.extension_filter = extension_filter
        self.file_data = []

    def scan_files(self):
        for foldername, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                if self.extension_filter and not filename.endswith(self.extension_filter):
                    continue
                filepath = os.path.join(foldername, filename)
                try:
                    size = os.path.getsize(filepath)
                    self.file_data.append((filename, filepath, size))
                except (FileNotFoundError, PermissionError):
                    continue

    def display_sorted(self):
        if not self.file_data:
            print("🚫 No files found.")
            return

        # Sort by size (descending)
        self.file_data.sort(key=lambda x: x[2], reverse=True)

        # Header
        print(f"{'File Name':<30} | {'Size (KB)':>10} | {'Path'}")
        print("-" * 80)

        for name, path, size in self.file_data:
            print(f"{name:<30} | {size/1024:>10.2f} | {path}")

def main():
    folder = input("📁 Enter directory to scan: ").strip()
    extension = input("📄 Filter by extension (e.g. .py) or press Enter to skip: ").strip() or None

    scanner = FileScanner(folder, extension)
    scanner.scan_files()
    scanner.display_sorted()

if __name__ == "__main__":
    main()
