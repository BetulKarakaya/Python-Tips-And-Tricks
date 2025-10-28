import atexit
from datetime import datetime
import tempfile
import os

class SessionLogger:
    """Automatically logs when a session starts and ends using atexit."""

    def __init__(self):
        self.temp_dir = tempfile.gettempdir()
        self.log_file = os.path.join(self.temp_dir, "session_log.txt")

        self._log_start()
        # Register cleanup automatically
        atexit.register(self._log_end)

    def _log_start(self):
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"Session started at {datetime.now()}\n")
        print(f"Session started. Log file: {self.log_file}")

    def _log_end(self):
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"Session ended at {datetime.now()}\n\n")
        print("! Session end logged automatically.")

    def run_task(self):
        print("Running some important work...")
        for i in range(3):
            print(f"   - Step {i+1} completed")
    
    def run_task_again(self):
        print("Running some important work again...")
        for i in range(3):
            print(f"   - Step {i+1} completed")


def main():
    logger = SessionLogger()
    logger.run_task()
    logger.run_task_again()
    print("Program will now exit — cleanup handled automatically!")


if __name__ == "__main__":
    main()
