tasks = []
def add_task(task):
    tasks.append(task)
    print("Task added:", task)
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found")
def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
while True:
    print("\nTo-Do List Application")
    print("A. Add Task")
    print("B. Remove Task")
    print("C. Display Tasks")
    print("D. Quit")
    choice = input("Enter your choice (A/B/C/D): ")
    if choice == 'A':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == 'B':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == 'C':
        display_tasks()
    elif choice == 'D':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please choose A, B, C, or D.")