import json
import os

# File where tasks will be stored
TASKS_FILE = "tasks.json"

# -------------------------------
# Helper functions
# -------------------------------

def load_tasks():
    """Load tasks from the JSON file, or return empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# -------------------------------
# Core functionality
# -------------------------------

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"task": description, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {description}")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("📂 No tasks yet. Start by adding one!")
        return
    print("\n📝 To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def delete_task(index):
    """Delete a task by its index number."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted task: {removed['task']}")
    else:
        print("⚠️ Invalid task number. Please try again.")

def mark_done(index):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"✔️ Marked as done: {tasks[index - 1]['task']}")
    else:
        print("⚠️ Invalid task number. Please try again.")

# -------------------------------
# Main Menu
# -------------------------------

def main():
    while True:
        print("\n==== 📌 TO-DO LIST MENU ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        choice = input("👉 Choose an option (1-5): ").strip()

        if choice == "1":
            task = input("Enter task description: ").strip()
            if task:
                add_task(task)
            else:
                print("⚠️ Task cannot be empty.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            view_tasks()
            try:
                index = int(input("Enter task number to mark as done: "))
                mark_done(index)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "5":
            print("👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()

