import traceback
from pathlib import Path
from datetime import datetime

class ErrorLogger:
    def __init__(self, log_dir="logs", log_file="error.log"):
        self.log_path = Path(log_dir)
        self.log_path.mkdir(exist_ok=True)  #Create log directory if it doesn't exist
        self.log_file = self.log_path / log_file

    def run_with_log(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_details = traceback.format_exc()
            log_entry = f"\n[{timestamp}] An error occurred:\n{error_details}"
            self.log_file.write_text(log_entry, encoding="utf-8")
            print("An error occurred. Check the log file for details.")
            return None

def risky_operation():
    print("Enter a number to divide 100:")
    x = int(input("➗ Number: ")) # If the user enters something invalid, an error occurs
    return 100 / x

def main():
    logger = ErrorLogger()
    logger.run_with_log(risky_operation)

if __name__ == "__main__":
    main()