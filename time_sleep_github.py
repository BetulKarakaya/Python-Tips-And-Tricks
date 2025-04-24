import time

class Reminder:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, delay_sec):
        # Add a task with its delay time
        self.tasks.append((task, delay_sec))
        print(f"📝 Task added: '{task}' will remind you in {delay_sec} seconds.")

    def start(self):
        print("\n⏰ Reminder System Started!\n")
        for task, delay in self.tasks:
            print(f"⏳ Waiting for {delay} seconds to remind you about: {task}")
            time.sleep(delay)
            print(f"🔔 Reminder: {task}!\n")

def main():
    app = Reminder()
    app.add_task("Drink water 💧", 3)
    app.add_task("Stretch your legs 🦵", 5)
    app.add_task("Back to focus! 💻", 2)
    
    app.start()

if __name__ == "__main__":
    main()
