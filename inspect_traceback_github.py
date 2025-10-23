import inspect
import traceback
from datetime import datetime

class SmartErrorTracker:
    """Automatically logs and explains runtime errors with function context."""

    def __init__(self, log_file="error_log.txt"):
        self.log_file = log_file

    def safe_execute(self, func, *args, **kwargs):
        """Execute a function and log detailed info if an error occurs."""
        try:
            return func(*args, **kwargs)
        except Exception as e:
            frame = inspect.currentframe().f_back
            func_name = frame.f_code.co_name
            tb_info = traceback.format_exc()

            error_message = (
                f"\n-{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"-Function: {func_name}\n"
                f"-Error Type: {type(e).__name__}\n"
                f"-Traceback:\n{tb_info}\n"
            )

            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(error_message)

            print("Error logged! Check 'error_log.txt' for details.\n")
            print(error_message)


class MathOperations:
    """Performs risky mathematical operations."""

    def divide(self, a, b):
        """Divide two numbers safely."""
        return a / b

    def power(self, base, exp):
        """Raise a number to a power."""
        return base ** exp


def main():
    tracker = SmartErrorTracker()
    math_ops = MathOperations()

    tracker.safe_execute(math_ops.divide, 10, 0)     # Division by zero
    tracker.safe_execute(math_ops.power, 5, "three") # Invalid type


if __name__ == "__main__":
    main()
