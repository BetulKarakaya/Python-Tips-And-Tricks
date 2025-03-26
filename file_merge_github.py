import os

class FileMerger:
    def __init__(self, directory, extension, output_file):
       
        self.directory = directory
        if not extension.startswith("."):
            extension = "." + extension 
        self.extension = extension
        self.output_file = output_file
        self.files_to_merge = []

    def find_files(self):
      
        self.files_to_merge = [
            f for f in os.listdir(self.directory) if f.endswith(self.extension)
        ]
        if not self.files_to_merge:
            print("⚠️ No matching files found!")
        else:
            print(f"📂 Found {len(self.files_to_merge)} '{self.extension}' files to merge.")

    def merge_files(self):
       
        if not self.files_to_merge:
            print("❌ No files to merge.")
            return
        
        with open(f"{self.directory}\{self.output_file}{self.extension}", "w", encoding="utf-8") as outfile:
            for file in self.files_to_merge:
                file_path = os.path.join(self.directory, file)
                with open(file_path, "r", encoding="utf-8") as infile:
                    content = infile.read()
                    outfile.write(f"\n--- {file} ---\n")
                    outfile.write(content)
                    outfile.write("\n")
        
        print(f"✅ Merging completed! Output saved to '{self.output_file}'")

    def run(self):
        
        self.find_files()
        self.merge_files()


def main():
    directory = input("📁 Enter the directory path: ").strip()
    extension = input("🔍 Enter the file extension (e.g., .txt, .log): ").strip()
    output_file = input("💾 Enter the output file name (e.g., merged.txt): ").strip()

    app = FileMerger(directory, extension, output_file)
    app.run()


if __name__ == "__main__":
    main()
