import inspect

class FunctionAnalyzer:
    """Analyze a function's signature and auto-generate a sample call."""

    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def show_signature(self):
        print(f"Function Name: {self.func.__name__}")
        print("Signature:")
        for name, param in self.signature.parameters.items():
            print(f"  - {name}: {param}")
        print("\nReturn Annotation:", self.signature.return_annotation)

    def generate_sample_call(self):
        """Auto-create a mock call example based on parameter names."""
        sample_args = []
        for name, param in self.signature.parameters.items():
            if param.default is not inspect.Parameter.empty:
                sample_args.append(f"{name}={param.default!r}")
            else:
                sample_args.append(f"{name}='example'")
        call = f"{self.func.__name__}({', '.join(sample_args)})"
        print(f"\nSuggested Call:\n{call}")

# Example function to analyze
def register_user(username: str, email: str, active: bool = True, role: str = "User") -> dict:
    """Registers a new user and returns a user dictionary."""
    return {"username": username, "email": email, "active": active, "role": role}

def main():
    analyzer = FunctionAnalyzer(register_user)
    analyzer.show_signature()
    analyzer.generate_sample_call()

if __name__ == "__main__":
    main()
