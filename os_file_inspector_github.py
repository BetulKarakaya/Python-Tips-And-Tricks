import os
import datetime

class FileInspector:
    def __init__(self, directory):
        self.directory = directory

    def display_file_info(self):
        if not os.path.exists(self.directory):
            print("❌ The directory does not exist.")
            return
        
        print("\n📁 File Information Table\n")
        headers = ["File Name", "Size (KB)", "Created", "Last Modified"]
        col_widths = [30, 12, 22, 22]
        print("|".join(h.center(w) for h, w in zip(headers, col_widths)))
        print("-" * (sum(col_widths) + len(col_widths) - 1))
        
        for filename in os.listdir(self.directory):
            full_path = os.path.join(self.directory, filename)
            if os.path.isfile(full_path):
                size_kb = round(os.path.getsize(full_path) / 1024, 2)
                created = datetime.datetime.fromtimestamp(os.path.getctime(full_path)).strftime('%Y-%m-%d %H:%M:%S')
                modified = datetime.datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M:%S')

                row = [
                    filename[:28].ljust(col_widths[0]),  # Truncate long file names
                    f"{size_kb}".center(col_widths[1]),
                    created.center(col_widths[2]),
                    modified.center(col_widths[3]),
                ]
                print("|".join(row))


def main():
    path = input("📂 Enter a directory path: ").strip()
    inspector = FileInspector(path)
    inspector.display_file_info()

if __name__ == "__main__":
    main()
