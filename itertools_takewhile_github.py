from itertools import takewhile

class HeartRateMonitor:
    def __init__(self, heart_rates, safe_limit):
        self.heart_rates = heart_rates
        self.safe_limit = safe_limit

    def safe_session_data(self):
        """
        Returns heart rate data while it stays below the safe limit.
        """
        return list(takewhile(lambda x: x < self.safe_limit, self.heart_rates))

    def display(self):
        print(f"Safe heart rate session (limit: {self.safe_limit} bpm):\n")
        for i, bpm in enumerate(self.safe_session_data(), 1):
            print(f"Minute {i}: {bpm} bpm")
        print("Safety limit exceeded, data collection stopped.")

def main():

    session = [82, 88, 93, 97, 102, 108, 115, 122, 127]

    monitor = HeartRateMonitor(session, safe_limit=110)
    monitor.display()

if __name__ == "__main__":
    main()