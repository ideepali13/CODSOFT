import json
import os

# Define the file path for persistent storage
FILE_PATH = "todo_list.json"

def load_tasks():
    """Loads tasks from the JSON file, or returns an empty list if the file doesn't exist."""
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Handle case where file is empty or corrupted
            return []
    return []

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Displays all tasks with their status (Completed/Pending)."""
    if not tasks:
        print("\nYour To-Do List is currently empty! Time to add a task.")
        return

    print("\n--- Current To-Do List ---")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "⏳"
        print(f"{i}. {status} {task['description']}")
    print("--------------------------")

def add_task(tasks):
    """Adds a new task to the list."""
    description = input("Enter the new task description: ").strip()
    if description:
        tasks.append({"description": description, "completed": False})
        save_tasks(tasks)
        print(f"Task '{description}' added successfully.")
    else:
        print("Task description cannot be empty.")

def mark_complete(tasks):
    """Marks a specified task as completed."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to mark as COMPLETE: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            save_tasks(tasks)
            print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a specified task from the list."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to DELETE: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['description']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def todo_app():
    """Main application loop."""
    tasks = load_tasks()

    while True:
        print("\n" + "="*40)
        print("    **To-Do List Manager**")
        print("="*40)
        print("Choose an option:")
        print("1. View To-Do List")
        print("2. Add New Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        print("="*40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nTasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_app()