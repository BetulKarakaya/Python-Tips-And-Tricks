from contextlib import redirect_stdout
from pathlib import Path
from datetime import datetime

class Logger:
    def __init__(self, filename="log_redirect_stdout.txt"):
        self.log_file = Path(filename)

    def log_process(self, func):
        with self.log_file.open("a", encoding="utf-8") as f, redirect_stdout(f):
            print(f"\n--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
            func()
            print("--- End of Log ---\n")

def system_check():
    print("- Checking system...")
    print("- Connecting to server...")
    print("- System OK.")

def main():
    logger = Logger()
    logger.log_process(system_check)

    print("✅ System check completed. Log saved silently.")

if __name__ == "__main__":
    main()