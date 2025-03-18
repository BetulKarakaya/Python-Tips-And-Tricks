from collections import deque
import time

class TaskManager:
    def __init__(self):
        # 📝 Deque (Double-Ended Queue) is a list-like container with fast O(1) appends and pops from both ends.
        # It is optimized for queue and stack operations, making it more efficient than a regular list in such use cases.
        self.tasks = deque()  
        
    def add_task(self, task):
        
        self.tasks.append(task)
        print(f"✅ Task added: {task} (Total tasks: {len(self.tasks)})")
    
    def complete_task(self):
        
        if self.tasks:
            completed = self.tasks.popleft() # Removes from the left end
            print(f"🎯 Task completed: {completed} (Remaining tasks: {len(self.tasks)})")
        else:
            print("⚠ No tasks left to complete!")
    
    def show_tasks(self):
       
        if not self.tasks:
            print("📭 No pending tasks!")
        else:
            print("\n📌 Pending Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"🔹 {i}. {task}")
    
    def run_simulation(self):
        
        self.add_task("Finish report")
        self.add_task("Reply to emails")
        self.add_task("Prepare presentation")
        
        self.show_tasks()
        
        time.sleep(1)  
        self.complete_task()
        
        time.sleep(1)
        self.complete_task()
        
        self.show_tasks()

def main():
    app = TaskManager()
    app.run_simulation()

if __name__ == "__main__":
    main()
