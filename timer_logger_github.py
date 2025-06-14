import time

class TimerLogger:
    
    def __init__(self, log_file="timer_log.txt"): 
        self.log_file = log_file

    def __enter__(self): 
        self.start = time.time()
        self._log("Timer started.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        duration = self.end - self.start
        self._log(f"Timer ended. Duration: {duration:.2f} seconds.")
        if exc_type:
            self._log(f"An exception occurred: {exc_type.__name__}: {exc_val}")
            return -1
        
    def _log(self, message):
        try:
            with open(self.log_file, "a", encoding="utf-8") as file:
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
            print(message)
        except Exception as e:
            print(f"Log error: {e}")

    def __str__(self):
        return f"TimerLogger writing to: {self.log_file}"
    
def main():
    
    print(TimerLogger())
    with TimerLogger():
        total = sum(i for i in range(10**6))  # Simulate some work

    with TimerLogger():
        x = 1 / 0  # Will log the exception

if __name__ == "__main__":
    main()
