import random
from datetime import datetime

def dream_vacation_planner():
    """
    Randomly generates a dream vacation plan with destination, activity, and duration.
    """
    # List of destinations, activities, and durations
    destinations = ["Bali, Indonesia 🌴", "Paris, France 🗼", "Kyoto, Japan 🏯", "Reykjavik, Iceland ❄️", "Sydney, Australia 🐨"]
    activities = ["snorkeling 🐠", "wine tasting 🍷", "hiking in the mountains 🥾", "visiting museums 🖼️", "relaxing at a luxury spa 🧖‍♀️"]
    durations = ["3 days", "1 week", "10 days", "2 weeks", "a long weekend"]

    # Randomly pick one from each category
    destination = random.choice(destinations)
    activity = random.choice(activities)
    duration = random.choice(durations)

    # Generate the plan
    today = datetime.now().strftime("%Y-%m-%d")
    vacation_plan = (
        f"✨ Dream Vacation Plan for {today} ✨\n"
        f"Destination: {destination}\n"
        f"Activity: {activity}\n"
        f"Duration: {duration}\n"
        f"Get packing and make it a reality! 🎒"
    )

    return vacation_plan

def main():
    print("🌍 Welcome to Your Dream Vacation Planner! 🏖️")
    print(dream_vacation_planner())

if __name__ == "__main__":
    main()
