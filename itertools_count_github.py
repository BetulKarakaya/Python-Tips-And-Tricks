from itertools import count
from datetime import datetime

class NoteManager:
    _id_counter = count(1)  #Starts from 1 and increases automatically

    def __init__(self):
        self.notes = {}

    def add_note(self, text):
        note_id = next(self._id_counter)
        self.notes[note_id] = {
            "text": text.strip(),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        print(f"Note #{note_id} added.")

    def list_notes(self):
        if not self.notes:
            print("No notes yet.")
        for note_id, info in self.notes.items():
            print(f"\n# Note #{note_id}")
            print(f"   - Text: {info['text']}")
            print(f"   - Time: {info['created_at']}")

def main():
    manager = NoteManager()
    manager.add_note("Remember the meeting at 3 PM")
    manager.add_note("Buy oat milk")
    manager.list_notes()

if __name__ == "__main__":
    main()