from collections import deque
import time

class TaskScheduler:
    def __init__(self):
        """ Initialize two queues: FIFO for normal tasks, LIFO for priority tasks. """
        self.tasks = deque()  # Normal tasks FIFO
        self.priority_tasks = []  # Priority tasks LIFO
        
    def add_task(self, task, priority=False):
        
        if priority:
            self.priority_tasks.append(task)  
            print(f"🔥 Priority task added: {task} (Total priority: {len(self.priority_tasks)})")
        else:
            self.tasks.append(task)  
            print(f"✅ Task added: {task} (Total tasks: {len(self.tasks)})")
    
    def execute_task(self):
    
        if self.priority_tasks:
            task = self.priority_tasks.pop()  
            print(f"⚡ Executing priority task: {task} (Remaining priority: {len(self.priority_tasks)})")
        elif self.tasks:
            task = self.tasks.popleft()  
            print(f"⏳ Executing task: {task} (Remaining tasks: {len(self.tasks)})")
        else:
            print("⚠️ No tasks left to execute!")
    
    def show_tasks(self):
     
        print("\n🔍 Task Overview:")
        for i, task in enumerate(reversed(self.priority_tasks), 1):
            print(f"🔥 {i}. {task} (PRIORITY)")
        for i, task in enumerate(self.tasks, len(self.priority_tasks) + 1):
            print(f"🔹 {i}. {task}")
    
    def run_simulation(self):
   
        self.add_task("Check emails")
        self.add_task("Fix bug in code", priority=True)
        self.add_task("Write documentation")
        self.add_task("Deploy update", priority=True)
        
        self.show_tasks()
        
        time.sleep(1)
        self.execute_task()
        
        time.sleep(1)
        self.execute_task()
        
        self.show_tasks()

def main():
    app = TaskScheduler()
    app.run_simulation()

if __name__ == "__main__":
    main()
