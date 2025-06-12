class DataWrapper:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        # Allow flexible access using both int and string keys
        if isinstance(key, int):
            try:
                return list(self._data.values())[key]
            except IndexError:
                return "❌ Index out of range"
        elif isinstance(key, str):
            return self._data.get(key, "❌ Key not found")
        else:
            raise TypeError("Key must be int or str")

    def __str__(self):
        return f"DataWrapper with keys: {list(self._data.keys())}"

# Example usage
info = DataWrapper({
    "name": "Betül",
    "job": "Data Scientist",
    "language": "Python"
})

print(info["name"])   # Access with string key
print(info[1])        # Access with index (int)
print(info[10])       # Index out of range, returns friendly error
print(info["city"])   # Key not found
print(info[2])        # Python
