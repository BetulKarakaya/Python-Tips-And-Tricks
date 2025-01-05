import os
import math
from datetime import datetime
import psutil  # Ensure psutil is installed (`pip install psutil`)

def log_system_performance():
    """
    Logs the square root of the system's uptime along with the current date and time.
    Demonstrates the use of psutil, math, and datetime modules.
    """
    try:
        # Get system uptime using psutil.boot_time() and the current time
        current_time_unix = datetime.now().timestamp()
        uptime_seconds = current_time_unix - psutil.boot_time()

        # Calculate the square root of the uptime using the math.sqrt() function
        uptime_sqrt = math.sqrt(uptime_seconds)

        # Get the current date and time in a human-readable format
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Prepare the log entry
        log_entry = f"[{current_time}] System Uptime (sqrt): {uptime_sqrt:.2f} seconds\n"

        # Save the log entry to a file
        with open("system_performance_log.txt", "a") as file:
            file.write(log_entry)
            print(f"Log entry saved: {log_entry.strip()}")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    log_system_performance()


if __name__ == "__main__":
    main()
