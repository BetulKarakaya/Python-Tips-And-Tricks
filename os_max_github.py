import os

class LargestFileFinder:
    def __init__(self, root_path):
        if os.path.isdir(root_path):
            self.root_path = root_path
        else:
            raise NotADirectoryError("❌ This path is not a valid directory.")
        self.largest_file = ("", 0)  # (path, size)

    def find_largest(self):
        for dirpath, _, filenames in os.walk(self.root_path):
            for file in filenames:
                try:
                    full_path = os.path.join(dirpath, file)
                    size = os.path.getsize(full_path)
                    if size > self.largest_file[1]:
                        self.largest_file = (full_path, size)
                except Exception as e:
                    print(f"⚠️ Skipped: {file} due to {e}")

    @staticmethod
    def human_readable_size(size_in_bytes):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_in_bytes < 1024:
                return f"{size_in_bytes:.2f} {unit}"
            size_in_bytes /= 1024
        return f"{size_in_bytes:.2f} PB"

    def display_result(self):
        path, size = self.largest_file
        if path:
            print(f"\n📦 Largest file found:")
            print(f"📄 File: {path}")
            print(f"📏 Size: {self.human_readable_size(size)}")
        else:
            print("🤷 No files found in the specified directory.")

def main():
    print("🔍 Welcome to the Largest File Finder App!")
    path = input("📁 Enter a folder path to scan: ").strip()

    try:
        app = LargestFileFinder(path)
        app.find_largest()
        app.display_result()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
