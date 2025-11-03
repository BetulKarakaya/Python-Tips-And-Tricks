import sys
import importlib

class ModuleInspector:
    """Explore and safely manipulate Python's module cache (sys.modules)."""

    def __init__(self):
        print(f"Currently loaded modules: {len(sys.modules)}")

    def check_module(self, name: str):
        """Check if a module is currently loaded."""
        if name in sys.modules:
            print(f"- '{name}' is currently loaded.")
        else:
            print(f"⚠️ '{name}' is NOT loaded yet.")

    def unload_module(self, name: str):
        """Safely unload a module from memory."""
        if name in sys.modules:
            del sys.modules[name]
            print(f"- Module '{name}' has been unloaded from sys.modules.")
        else:
            print(f"⚠️ Module '{name}' was not loaded.")

    def reload_module(self, name: str):
        """Reload a module dynamically using importlib."""
        print(f"Reloading module '{name}' ...")
        module = importlib.import_module(name)
        reloaded = importlib.reload(module)
        print(f"Module '{name}' reloaded successfully.")
        return reloaded


def main():
    inspector = ModuleInspector()

    module_name = "math"

    # Check if math is loaded
    inspector.check_module(module_name)

    # Use math
    import math
    print("\nUsing math module:")
    print("   √25 =", math.sqrt(25))

    # Unload and reload math dynamically
    inspector.unload_module(module_name)
    inspector.check_module(module_name)

    math = inspector.reload_module(module_name)
    print("   √49 =", math.sqrt(49))


if __name__ == "__main__":
    main()
