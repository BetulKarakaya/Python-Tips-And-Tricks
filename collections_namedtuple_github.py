from collections import namedtuple

Activity = namedtuple("Activity", ["date", "name", "duration"])

class ActivityTracker:
    def __init__(self):
        self.records = []

    def add_activity(self, date, name, duration):
        activity = Activity(date, name, duration)
        self.records.append(activity)
        print(f"+ Added: {activity.name} on {activity.date} ({activity.duration} min)")

    def list_activities(self):
        if not self.records:
            print("No activities recorded.")
            return
        print("\n- Activity Log:")
        for act in self.records:
            print(f" - {act.date}: {act.name} ({act.duration} min)")

def main():
    tracker = ActivityTracker()
    tracker.add_activity("2025-06-23", "Coding", 90)
    tracker.add_activity("2025-06-23", "Reading", 30)
    tracker.add_activity("2025-06-24", "Exercise", 45)
    tracker.list_activities()

if __name__ == "__main__":
    main()