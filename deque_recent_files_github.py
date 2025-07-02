from collections import deque

class RecentFiles:
    def __init__(self, max_files=5):
        self.history = deque(maxlen=max_files)  #Limits the number of stored items

    def open_file(self, filename):
        self.history.appendleft(filename)
        print(f"- Opened: {filename}")

    def show_recent(self):
        print("\n* Recent Files:")
        if not self.history:
            print("No files opened yet!")
        for i, file in enumerate(self.history, 1):
            print(f"  {i}. {file}")

def main():
    recent = RecentFiles()

    recent.open_file("report.docx")
    recent.open_file("slides.pptx")
    recent.open_file("data.csv")
    recent.open_file("notes.txt")
    recent.open_file("todo.md")
    recent.open_file("final_report.pdf")

    recent.show_recent()

if __name__ == "__main__":
    main()