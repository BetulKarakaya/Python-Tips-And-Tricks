import datetime
import os

def add_event(events):
    """
    Adds a new event to the events dictionary.
    """
    date_str = input("Enter the event date (YYYY-MM-DD): ")
    try:
        event_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        event_name = input("Enter the event name: ")
        events[event_date] = event_name
        print(f"Event '{event_name}' added on {event_date}!")
    except ValueError:
        print("Invalid date format. Please try again.")

def view_events(events):
    """
    Displays all events sorted by date.
    """
    if not events:
        print("No events added yet.")
    else:
        print("\nUpcoming Events:")
        for date in sorted(events):
            print(f"{date}: {events[date]}")
        print("\n")

def save_events_to_file(events, filename="events_log.txt"):
    """
    Saves all events to a text file.
    """
    try:
        with open(filename, "w") as file:
            for date, name in sorted(events.items()):
                file.write(f"{date}: {name}\n")
        print(f"Events saved to {filename}")
    except Exception as e:
        print(f"Error saving events: {e}")

def load_events_from_file(filename="events_log.txt"):
    """
    Loads events from a text file if it exists.
    """
    events = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                try:
                    date_str, name = line.strip().split(": ")
                    events[datetime.datetime.strptime(date_str, "%Y-%m-%d").date()] = name
                except ValueError:
                    continue
    return events

def main():
    print("🎉 Welcome to Your Personal Event Calendar 🎉")
    events = load_events_from_file()
    
    while True:
        print("\nMenu:")
        print("1. Add Event")
        print("2. View Events")
        print("3. Save and Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_event(events)
        elif choice == "2":
            view_events(events)
        elif choice == "3":
            save_events_to_file(events)
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
