from contextlib import ExitStack

class MultiFileReader:
    def __init__(self, file_paths: list[str]):
        self.file_paths = file_paths

    def read_files(self):
        """Dynamically manage multiple file contexts safely."""
        with ExitStack() as stack:
            files = [stack.enter_context(open(path, "r", encoding="utf-8")) for path in self.file_paths]
            print("- Reading all files safely:\n")
            for file in files:
                print(f"--- {file.name} ---")
                print(file.read())
                print()

def main():
    # Creating sample files for demo
    paths = ["file1.txt", "file2.txt", "file3.txt"]
    for i, path in enumerate(paths, 1):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"This is content of file {i}")

    reader = MultiFileReader(paths)
    reader.read_files()

if __name__ == "__main__":
    main()
