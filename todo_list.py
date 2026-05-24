def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks(tasks):
    print("\n--- Your Tasks ---")
    for task in tasks:
        print("- " + task)

def main():
    tasks = []
    while True:
        print("\n1. Add | 2. View | 3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            print("Bye!")
            break
        else:
            print("Invalid!")

main()
