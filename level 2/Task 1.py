import json
import os

TASKS_FILE = "tasks.json"


# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {description}")


# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return

    print("\n📌 To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['description']} [{status}]")


# Delete a task
def delete_task(index):
    tasks = load_tasks()
    try:
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {removed_task['description']}")
    except IndexError:
        print("⚠️ Invalid task number!")


# Mark task as done
def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"✅ Task marked as done: {tasks[index - 1]['description']}")
    except IndexError:
        print("⚠️ Invalid task number!")


# Search tasks by keyword
def search_tasks(keyword):
    tasks = load_tasks()
    found = [t for t in tasks if keyword.lower() in t["description"].lower()]

    if not found:
        print(f"🔎 No tasks found containing '{keyword}'.")
        return

    print(f"\n🔎 Search Results for '{keyword}':")
    for i, task in enumerate(found, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['description']} [{status}]")


# Edit a task description
def edit_task(index, new_description):
    tasks = load_tasks()
    try:
        old_desc = tasks[index - 1]["description"]
        tasks[index - 1]["description"] = new_description
        save_tasks(tasks)
        print(f"✏️ Task updated: '{old_desc}' → '{new_description}'")
    except IndexError:
        print("⚠️ Invalid task number!")


# Main menu
def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Search Tasks")
        print("6. Edit Task")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            num = int(input("Enter task number to delete: "))
            delete_task(num)
        elif choice == "4":
            view_tasks()
            num = int(input("Enter task number to mark as done: "))
            mark_done(num)
        elif choice == "5":
            keyword = input("Enter keyword to search: ")
            search_tasks(keyword)
        elif choice == "6":
            view_tasks()
            num = int(input("Enter task number to edit: "))
            new_desc = input("Enter new description: ")
            edit_task(num, new_desc)
        elif choice == "7":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")


if __name__ == "__main__":
    main()
