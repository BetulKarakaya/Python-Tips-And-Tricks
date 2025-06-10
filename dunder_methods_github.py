class LoveNotes:
    def __init__(self, owner, notes=None):
        # Constructor: Initializes the LoveNotes object with an owner and an optional list of notes
        self.owner = owner
        self.notes = notes or []

    def __str__(self):
        # __str__: Returns a user-friendly string representation of the object (used in print)
        return f"{self.owner}'s sweet love notes 💌 ({len(self)} total)"

    def __repr__(self):
        # __repr__: Returns an unambiguous string representation of the object for debugging
        return f"LoveNotes(owner={self.owner!r}, notes={self.notes!r})"

    def __len__(self):
        # __len__: Returns the number of notes in the collection
        return len(self.notes)

    def __getitem__(self, index):
        # __getitem__: Allows indexing (e.g. obj[0]) to access a specific note
        return self.notes[index]

    def __contains__(self, note):
        # __contains__: Enables usage of 'in' to check if a note exists in the collection
        return note in self.notes

    def __eq__(self, other):
        # __eq__: Checks equality by comparing both owner and notes
        if not isinstance(other, LoveNotes):
            return False
        return self.owner == other.owner and self.notes == other.notes

    def __lt__(self, other):
        # __lt__: Allows comparison using '<' based on the number of notes
        return len(self) < len(other)

    def __call__(self, new_note):
        # __call__: Makes the object callable like a function to add a new note
        self.notes.append(new_note)
        print(f"📝 New note added to {self.owner}'s collection!")

# Example usage 💕
betul_notes = LoveNotes("Betül", ["You're amazing", "Don't forget to rest 💖"])
print(betul_notes)  # __str__

betul_notes("Keep shining ✨")  # __call__
print(len(betul_notes))        # __len__
print(betul_notes[0])          # __getitem__
print("Don't forget to rest 💖" in betul_notes)  # __contains__

# Comparing two LoveNotes objects
another_notes = LoveNotes("Betül", ["You're amazing", "Don't forget to rest 💖", "Keep shining ✨"])
print(betul_notes == another_notes)   # __eq__
print(betul_notes < LoveNotes("Aşkım", ["Hi"]))  # __lt__
