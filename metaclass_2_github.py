class DebugMeta(type):
    def __new__(mcs, name, bases, class_dict):
        print(f"- Creating class: {name}")
        print(f"- Bases: {[base.__name__ for base in bases]}")
        print(f"- Class Attributes and Methods:")
        for key, value in class_dict.items():
            print(f"   - {key}: {value}")
        print("*** Class creation complete. ***\n")
        return super().__new__(mcs, name, bases, class_dict)

#Parent Class
class Animal:
    def move(self):
        print("I'm moving")

#Child Class
class Bird(Animal, metaclass=DebugMeta):
    wings = 2

    def fly(self):
        print("I'm flying")

def main():
    b = Bird()
    b.fly()
    b.move()

if __name__ == "__main__":
    main()