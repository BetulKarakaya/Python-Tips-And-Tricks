class AttributeDict:
    """A dictionary that allows access to keys as attributes (dot notation)."""

    def __init__(self, data: dict):
        self._data = data

    def __getattr__(self, key):
        """Called when attribute is not found normally → look inside dictionary."""
        try:
            value = self._data[key]
            return AttributeDict(value) if isinstance(value, dict) else value
        except KeyError:
            raise AttributeError(f"'{key}' not found in AttributeDict")

    def __repr__(self):
        return f"AttributeDict({self._data})"


def main():
    user = AttributeDict({
        "name": "Betül",
        "skills": {
            "technical": ["Python", "C#", "TensorFlow"],
            "soft": ["Teamwork", "Problem-Solving"]
        },
        "age": 25
    })

    print("Name:", user.name)
    print("Age:", user.age)
    print("Technical Skills:", user.skills.technical)
    print("Soft Skills:", user.skills.soft)


if __name__ == "__main__":
    main()
