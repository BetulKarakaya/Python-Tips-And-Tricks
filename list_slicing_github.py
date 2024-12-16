# Define a simple function to slice tasks by named parts of the day
def get_tasks(tasks, part_of_day):
    """
    Return tasks based on the part of the day.
    """
    parts = {
        "morning": tasks[:2],  # First two tasks
        "afternoon": tasks[2:5],  # Tasks 3 to 5
        "evening": tasks[5:],  # Tasks 6 to end
    }
    return parts.get(part_of_day.lower(), "Invalid part of the day!")


def main():
    # Define a list of tasks for the day
    tasks = ["Breakfast", "Emails", "Coding", "Lunch", "Meeting", "Exercise", "Dinner"]
    
    # Try slicing by part of the day
    print("Morning tasks:", get_tasks(tasks,"morning"))
    print("Afternoon tasks:", get_tasks(tasks,"afternoon"))
    print("Evening tasks:", get_tasks(tasks,"evening"))
    print("Invalid input test:", get_tasks(tasks,"midnight"))  # Testing an invalid input


if __name__ == "__main__":
   main()