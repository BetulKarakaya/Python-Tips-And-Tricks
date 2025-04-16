import os

class DiskUsageAnalyzer:
    def __init__(self, root_path):
        self.total_size = 0
        self.file_count = 0
        self.folder_count = 0

        if os.path.isdir(root_path):
            self.root_path = root_path
        else:
            print("❌ The directory does not exist.")
            raise NotADirectoryError()

    def get_directory_size(self):
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            self.folder_count += len(dirnames)
            self.file_count += len(filenames)

            for f in filenames:
                file_path = os.path.join(dirpath, f)
                try:
                    if os.path.isfile(file_path):
                        self.total_size += os.path.getsize(file_path)
                except Exception as e:
                    print(f"⚠️ Could not access {file_path}: {e}")
        
        return self.total_size, self.file_count, self.folder_count

    @staticmethod
    def human_readable_size(size_in_bytes):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_in_bytes < 1024:
                return f"{size_in_bytes:.2f} {unit}"
            size_in_bytes /= 1024
        return f"{size_in_bytes:.2f} PB"

def main():
    path = input("📁 Enter a folder path to analyze: ").strip()
    try:
        app = DiskUsageAnalyzer(path)

        print("\n📊 Analyzing disk usage...\n")
        total_size, file_count, folder_count = app.get_directory_size()

        print("📂 Folder:", path)
        print("📄 Total files:", file_count)
        print("📁 Total folders:", folder_count)
        print("💽 Total size:", app.human_readable_size(total_size))
    except:
        print("❌ Please try again with a valid directory path.")

if __name__ == "__main__":
    main()
