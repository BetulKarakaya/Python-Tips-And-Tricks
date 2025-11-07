import weakref
import tempfile
from pathlib import Path
import os
import gc
import time

class FinalizerTempFile:
    """
    Create a temporary file and ensure it's deleted either:
     - when obj.cleanup() is called, or
     - automatically when the object is garbage-collected (via weakref.finalize).
    This avoids relying on __del__ and works well with reference cycles.
    """
    def __init__(self, name_prefix: str = "session_"):
        # create a temp file next to the script (if you prefer), here using system temp
        fd, path = tempfile.mkstemp(prefix=name_prefix, suffix=".txt")
        os.close(fd)  # we only need the path, we'll open later
        self.path = Path(path)
        print(f"-- Temp file created: {self.path}")

        # Register a finalizer that will delete the file when this object is GC'd
        # Note: storing the finalize object is optional; keeping it prevents premature GC of finalizer itself
        self._finalizer = weakref.finalize(self, self._cleanup_action, str(self.path))
        # You can check if finalizer is alive via self._finalizer.alive

    @staticmethod
    def _cleanup_action(path_str: str):
        """Actual cleanup executed when object is collected (or finalizer called)."""
        try:
            p = Path(path_str)
            if p.exists():
                p.unlink()
                print(f"- Temp file automatically deleted by finalizer: {p}")
            else:
                print(f"⚠️ Temp file already removed: {p}")
        except Exception as e:
            print(f"⚠️ Cleanup failed: {e}")

    def write(self, text: str):
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"- Wrote to temp file: {text}")

    def cleanup(self):
        """Manual cleanup (optional) — also invalidates the automatic finalizer."""
        if self._finalizer.alive:
            # Call finalizer now and prevent it from running twice
            self._finalizer()  # invokes _cleanup_action
            print("- Manual cleanup executed and finalizer invalidated.")
        else:
            print("- Finalizer already ran or was invalidated.")

def demo_auto_cleanup():
    print("\n--- demo_auto_cleanup (finalizer triggers on GC) ---")
    obj = FinalizerTempFile()
    obj.write("temporary data")
    # remove strong references to the object
    obj_ref = obj
    del obj
    # force garbage collection to demonstrate finalizer behaviour
    print("Forcing garbage collection...")
    gc.collect()
    time.sleep(0.1)  # give a tiny moment for finalizer to run (finalizers run in main thread)

def demo_manual_cleanup():
    print("\n--- demo_manual_cleanup (explicit cleanup) ---")
    obj = FinalizerTempFile()
    obj.write("more temporary data")
    # call manual cleanup
    obj.cleanup()
    # deleting the object now will not run cleanup again
    del obj
    gc.collect()
    time.sleep(0.1)

def main():
    demo_auto_cleanup()
    demo_manual_cleanup()
    print("\n-- Demos finished. If any temp files remain, they were intentionally left for inspection.")

if __name__ == "__main__":
    main()
