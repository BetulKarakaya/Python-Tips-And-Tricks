import inspect

class CodeInspector:
    def __init__(self, obj):
        self.obj = obj

    def show_info(self):
        """Display detailed info about the given object."""
        print(f"- Object Name: {self.obj.__name__}")
        print(f"- Source File: {inspect.getsourcefile(self.obj)}")
        print(f"- Lines of Code: {len(inspect.getsourcelines(self.obj)[0])}")
        print("- Source Preview:\n")
        print("".join(inspect.getsourcelines(self.obj)[0]))

def sample_function(x, y):
    return x * y + 3

def main():
    inspector = CodeInspector(sample_function)
    inspector.show_info()

if __name__ == "__main__":
    main()
