import uuid
from datetime import datetime

class Note:
    def __init__(self, content):
        self.id = str(uuid.uuid4())  #Universally Unique ID
        self.content = content
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    def display(self):
        print(f"* {self.id}")
        print(f"* {self.created_at}")
        print(f"* {self.content}\n")

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, text):
        note = Note(text)
        self.notes.append(note)
        print("- Note added!\n")
        note.display()

    def list_notes(self):
        if not self.notes:
            print("No notes yet.")
        else:
            print("All Notes:\n")
            for note in self.notes:
                note.display()

def main():
    manager = NoteManager()
    manager.add_note("Learn Python tricks every day!")
    manager.add_note("Don't forget to hydrate ☕")
    manager.list_notes()

if __name__ == "__main__":
    main()