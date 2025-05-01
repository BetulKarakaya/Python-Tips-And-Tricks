import os

"""
💡 Advanced Tips & Tricks: Automatic File Renamer Tool with Class

⚠️ WARNING: This script makes **permanent changes** to the file system by renaming files.
It is recommended to test it on a copy of your folder before running it on important data.

📌 Description:
- This script automatically renames all files in a given directory using a specified prefix and optional file extension filter.
- Files are renamed in ascending numeric order (e.g., photo_1.jpg, photo_2.jpg, ...).
- Uses error handling to avoid crashes and provide helpful feedback.

🎯 Level: Advanced
- Demonstrates real-world use of class design, user input handling, file system operations, and error management.
"""

class AutoFileRenamer:
    def __init__(self, folder_path, prefix="file", extension=None):
        if not os.path.isdir(folder_path):
            raise NotADirectoryError("❌ The specified folder does not exist.")
        self.folder_path = folder_path
        self.prefix = prefix
        self.extension = extension

    def rename_files(self):
        files = sorted(os.listdir(self.folder_path))
        renamed_count = 0

        for index, filename in enumerate(files, start=1):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                if self.extension and ext.lower() != self.extension.lower():
                    continue
                new_name = f"{self.prefix}_{index}{ext}"
                new_path = os.path.join(self.folder_path, new_name)
                try:
                    os.rename(file_path, new_path)
                    renamed_count += 1
                    print(f"✅ Renamed: {filename} → {new_name}")
                except Exception as e:
                    print(f"⚠️ Failed to rename {filename}: {e}")

        print(f"\n🎉 Done! Total renamed: {renamed_count}")

def main():
    print("🔁 Welcome to the Automatic File Renamer App!")
    folder = input("📁 Enter folder path: ").strip()
    prefix = input("📝 Enter prefix (default: file): ").strip() or "file"
    ext = input("🔍 Filter by extension (e.g. .jpg) or leave blank: ").strip()

    try:
        app = AutoFileRenamer(folder_path=folder, prefix=prefix, extension=ext if ext else None)
        app.rename_files()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
