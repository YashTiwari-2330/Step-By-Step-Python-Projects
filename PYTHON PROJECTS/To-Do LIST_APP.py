tasks = []                                           # EMPTY TASK

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("📭 No tasks yet.")
    else:
        for i, (task, done) in enumerate(tasks, 1):
            status = "✅" if done else "❌"
            print(f"{i}. {task} [{status}]")

while True:
    show_menu()
    choice = input("Choose (1-5): ")

    if choice == '1':
        task = input("Enter task name: ")
        tasks.append((task, False))
        print("Task added!")

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        view_tasks()
        index = int(input("Task number to complete: ")) - 1
        if 0 <= index < len(tasks):
            task = tasks[index][0]
            tasks[index] = (task, True)
            print("Marked as complete!")

    elif choice == '4':
        view_tasks()
        index = int(input("Task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Deleted: {tasks.pop(index)[0]}")

    elif choice == '5':
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please enter 1–5.")
