# Function to view tasks
def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks yet. File not found.")


# Function to add a task
def add_task():
    task = input("Enter the task to add: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")


# Function to remove a task
def remove_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to remove.")
            return

        view_tasks()
        task_num = int(input("Enter the task number to remove: "))

        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Removed task: {removed.strip()}")
        else:
            print("Invalid task number.")
    except (FileNotFoundError, ValueError):
        print("Error: Couldn't remove task.")


# Main menu loop
while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid input. Please enter 1-4.")