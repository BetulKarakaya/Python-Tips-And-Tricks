class DynamicPerson:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, attr):
        return f"'{attr}' is not a defined attribute for this object."

def main():
    person = DynamicPerson("Alice", 30)
    print(person.name)  # Alice
    print(person.age)   # 30
    print(person.hobby) # __getattr__ is triggered

if __name__ == "__main__":
    main()
