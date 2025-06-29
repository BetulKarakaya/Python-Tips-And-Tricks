from itertools import cycle

class TaskAssigner:
    def __init__(self, members):
        self.members = cycle(members)  # ⏳ Endless Cycle: Ahmet → Ayşe → Zeynep → Ahmet...

    def assign_task(self, task_name):
        person = next(self.members)
        print(f"📝 Task '{task_name}' assigned to: {person}")


def main():
    team = ["Ahmet", "Ayşe", "Zeynep"]
    assigner = TaskAssigner(team)


    assigner.assign_task("Check server status")
    assigner.assign_task("Update spreadsheet")
    assigner.assign_task("Review design")
    assigner.assign_task("Fix bugs")

if __name__ == "__main__":
    main()