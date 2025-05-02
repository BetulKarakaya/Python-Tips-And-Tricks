import os
from collections import defaultdict

class FileExtensionCounter:
    def __init__(self, folder_path):
        if os.path.isdir(folder_path):
            self.folder = folder_path
        else:
            raise NotADirectoryError("❌ The given path is not a directory!")
        self.extension_stats = defaultdict(int)

    def count_extensions(self):
        for _, _, files in os.walk(self.folder):
            for file in files:
                _, ext = os.path.splitext(file)
                ext = ext.lower() or "no_extension"
                self.extension_stats[ext] += 1
        return dict(self.extension_stats)

    def display_stats(self):
        print("📊 File Extension Summary:\n")
        for ext, count in sorted(self.extension_stats.items(), key=lambda x: -x[1]):
            print(f"🔹 {ext:<10} --> {count} file(s)")

def main():
    try:
        path = input("📁 Enter the folder path you want to scan: ").strip()
        app = FileExtensionCounter(path)
        app.count_extensions()
        app.display_stats()
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
