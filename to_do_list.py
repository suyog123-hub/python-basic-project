print("=" * 40)
print("        SIMPLE TO-DO LIST")
print("=" * 40)

todo_list = []

while True:
    print("\n--- MENU ---")
    print("1 → Add a task")
    print("2 → View all tasks")
    print("3 → Mark a task as completed")
    print("4 → Delete a task")
    print("5 → Exit")
    
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 5:
        print("Exiting... Goodbye!")
        break

    elif choice == 1:
        task = input("Enter the task you want to add: ").strip()
        if task:
            todo_list.append(task)
            print(f"'{task}' added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == 2:
        if not todo_list:
            print("📭 Your to-do list is empty.")
        else:
            print("\nYour tasks:")
            for idx, task in enumerate(todo_list, start=1):
                print(f"   {idx}. {task}")

    elif choice == 3:
        if not todo_list:
            print("📭 Your list is empty. Nothing to mark as completed.")
            continue
        print("\nTasks:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"   {idx}. {task}")
        try:
            task_num = int(input("Enter the number of the completed task: "))
            if 1 <= task_num <= len(todo_list):
                completed = todo_list.pop(task_num - 1)
                print(f"Congratulations! You completed '{completed}'.")
                if not todo_list:
                    print("You have no pending tasks. Great job!")
            else:
                print(" Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == 4:
        if not todo_list:
            print("Your list is empty. Nothing to delete.")
            continue
        print("\nTasks:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"   {idx}. {task}")
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"'{removed}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Invalid choice. Please select 1-5.")