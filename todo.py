import json
from datetime import datetime

DATA_FILE = "tasks.json"


def load_tasks():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    title = input("Enter task description: ").strip()

    if not title:
        print("Task cannot be empty.\n")
        return

    task = {
        "title": title,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f'Added: "{title}"\n')


def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.\n")
        return

    print("\n--- Your To-Do List ---")

    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else " "

        print(
            f'{i}. [{status}] {task["title"]} '
            f'(added {task["created"]})'
        )

    print()


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        num = int(input("Enter task number to mark as complete: "))

        if num < 1 or num > len(tasks):
            raise IndexError

        tasks[num - 1]["done"] = True
        save_tasks(tasks)

        print(
            f'Marked "{tasks[num - 1]["title"]}" as complete.\n'
        )

    except (ValueError, IndexError):
        print("Invalid task number.\n")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))

        if num < 1 or num > len(tasks):
            raise IndexError

        removed = tasks.pop(num - 1)
        save_tasks(tasks)

        print(f'Deleted: "{removed["title"]}"\n')

    except (ValueError, IndexError):
        print("Invalid task number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("""
==== TO-DO LIST APP ====

1. View tasks
2. Add task
3. Mark task as complete
4. Delete task
5. Exit
""")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.\n")


if __name__ == "__main__":
    main()