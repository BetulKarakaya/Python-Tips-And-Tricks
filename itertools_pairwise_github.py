from itertools import pairwise
from datetime import datetime


class StepTracker:
    def __init__(self, steps_by_day: dict):
        """
        steps_by_day: {"2025-06-21": 3200, "2025-06-22": 4100, ...}
        """
        self.steps_by_day = dict(sorted(steps_by_day.items()))
    
    def analyze(self):
        print("🚶 Step Trend Report:\n")
        for (day1, steps1), (day2, steps2) in pairwise(self.steps_by_day.items()):
            change = steps2 - steps1
            emoji = "📈" if change > 0 else "📉" if change < 0 else "➖"
            summary = f"{day1} → {day2} {emoji} Δ {change:+} steps"
            print(summary)

    def average_steps(self):
        avg = sum(self.steps_by_day.values()) / len(self.steps_by_day)
        return round(avg, 2)

    def latest_entry(self):
        last_date = max(self.steps_by_day)
        return f"Latest entry: {last_date} — {self.steps_by_day[last_date]} steps"

if __name__ == "__main__":
  
    weekly_steps = {
        "2025-06-20": 4200,
        "2025-06-21": 4800,
        "2025-06-22": 4500,
        "2025-06-23": 5100,
        "2025-06-24": 4700
    }

    tracker = StepTracker(weekly_steps)

    print(tracker.latest_entry())
    print(f"Weekly Average: {tracker.average_steps()} steps\n")
    tracker.analyze()
