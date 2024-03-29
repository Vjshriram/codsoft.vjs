def main():
    todo_list = []

    while True:
        print("\n---- To-Do List ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            task = input("\nEnter task: ")
            todo_list.append({"task": task, "completed": False})
            print("Task added!")

        elif choice == "2":
            print("\nTasks:")
            for index, todo in enumerate(todo_list, start=1):
                status = "Done" if todo["completed"] else "Pending"
                print(f"{index}. {todo['task']} - {status}")

        elif choice == "3":
            task_index = int(input("\nEnter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(todo_list):
                todo_list[task_index]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

        elif choice == "4":
            task_index = int(input("\nEnter the task number to remove: ")) - 1
            if 0 <= task_index < len(todo_list):
                del todo_list[task_index]
                print("Task removed!")
            else:
                print("Invalid task number!")

        elif choice == "5":
            break

        else:
            print("Invalid choice! Please try again.")

    print("\nGoodbye!")


if __name__ == "__main__":
    main()
