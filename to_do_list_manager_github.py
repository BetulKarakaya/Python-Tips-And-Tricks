def todo_list_manager():
    """
    A simple to-do list manager where you can add, view, sort, and delete tasks.
    """
    print("📋 Welcome to Your Enhanced To-Do List Manager!")
    print("Let's organize your day efficiently. 🕒")
    
    # Initialize an empty list to store tasks
    tasks = []
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Sort tasks alphabetically")
        print("4. Delete a completed task")
        print("5. Exit")
        
        # Get the user's choice
        choice = input("Enter your choice (1/2/3/4/5): ").strip()
        
        match choice:
            case "1":
                tasks = add_task(tasks)
        
            case "2":
                list_tasks(tasks)
            
            case "3":
               tasks = sort_tasks(tasks)
        
            case "4":
                tasks = delete_completed_task(tasks)
        
            case "5":
                # Exit the program
                print("🚪 Exiting the To-Do List Manager. Have a productive day! 💪")
                break
            
            case _:
                raise Exception("Invalid Choose Input")

def add_task(task_list):
        try:
            task = input("Enter a task: ").strip()
            task_list.append(task)
            return task_list
        except:
            raise Exception("Something went wrong about adding new task")

def list_tasks(task_list):
        try:
            if not task_list:
                    print("📭 Your to-do list is empty!")
            else:
                print("\n📝 Here are your tasks:")
                for idx, task in enumerate(task_list, start=1):  # `enumerate` adds index numbers
                    print(f"{idx}. {task}")
        except:
            raise Exception("Something went wrong about listing tasks")

def sort_tasks(task_list):
    try:
        if task_list:
            task_list = sorted(task_list)  # `sorted` returns a sorted version of the list
            print("✨ Tasks sorted alphabetically!")
        else:
            print("📭 Your to-do list is empty. Add tasks to sort.")
        return task_list
    except:
        raise Exception("Something went wrong about sorting tasks alphabetically")
    
def delete_completed_task(task_list):
    if not task_list:
        print("📭 Your to-do list is empty! Nothing to delete.")
        return []
    else:
        print("\n📝 Here are your tasks:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
                
        try:
            task_to_delete = int(input("\nEnter the number of the task to delete: "))
            if 1 <= task_to_delete <= len(task_list):
                removed_task = task_list.pop(task_to_delete - 1)  # Remove task by index
                print(f"❌ '{removed_task}' has been removed from your to-do list!")
                return task_list
            else:
                    print("❌ Invalid task number. Please try again.")
            
            
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


if __name__ == "__main__":
    todo_list_manager()