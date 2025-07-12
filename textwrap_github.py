import textwrap

class NoteFormatter:
    def __init__(self, line_width=60):
        self.line_width = line_width

    def format_note(self, text):
        """Wraps long text into cleaner, readable lines."""
        return textwrap.fill(text, width=self.line_width)

def main():
    note = (
        "Python is a powerful programming language that's known for its simplicity, "
        "readability, and broad library support. It's widely used in web development, "
        "data science, automation, and more."
    )

    formatter = NoteFormatter()
    formatted = formatter.format_note(note)
    print("- Formatted Note:\n")
    print(formatted)

if __name__ == "__main__":
    main()