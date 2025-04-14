import os

class FolderTree:
    def __init__(self, root_path):
        self.root_path = root_path
        self.folder_count = 0
        self.file_count = 0

    def generate_tree(self, current_path=None, indent=""):
        if current_path is None:
            current_path = self.root_path

        try:
            entries = os.listdir(current_path)
        except PermissionError:
            print(f"{indent}🔒 Permission denied: {current_path}")
            return

        for entry in entries:
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path):
                print(f"{indent}📁 {entry}/")
                self.folder_count += 1
                self.generate_tree(full_path, indent + "    ")
            else:
                print(f"{indent}📄 {entry}")
                self.file_count += 1

    def display_summary(self):
        print("\n📊 Summary:")
        print(f"📁 Total folders: {self.folder_count}")
        print(f"📄 Total files  : {self.file_count}")

def main():
    folder = input("📂 Enter a directory path: ").strip()
    if not os.path.exists(folder):
        print("❌ Path does not exist.")
        return

    print("\n📌 Folder Tree:\n")
    tree = FolderTree(folder)
    tree.generate_tree()
    tree.display_summary()

if __name__ == "__main__":
    main()
