# todo_list_v2.py

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def list_tasks():
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i + 1}. {task['task']} ({status})")

def mark_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
    else:
        print("Invalid task index!")

#Added functionalities
def edit_task(task_index, new_task):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["task"] = new_task
    else:
        print("Invalid task index!")

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
    else:
        print("Invalid task index!")

if __name__ == "__main__":
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4.Edit Task")
        print("5.Delete Task")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            mark_completed(task_index)
        # Added functionalities ...
        elif choice == "4":
            task_index = int(input("Enter the task index to edit: ")) - 1
            new_task = input("Enter the new task description: ")
            edit_task(task_index, new_task)
        elif choice == "5":
            task_index = int(input("Enter the task index to delete: ")) - 1
            delete_task(task_index)
        elif choice == "0":
            break
        
        else:
            print("Invalid choice. Please try again.")





