# Simple To-Do List app

# List to Store Tasks
tasks = []

#function to add task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

#function to remove task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed!")
    else:
        print("task not found!")

# Function to view task
def view_tasks():
    if tasks:
        print("Your Tasks")
        for idx, task in enumerate(tasks, 1):  #Start numbering from 1
            print(f"{idx}. {task}")
    else:
        print("No tasks in your list!")

#Infinite loop to keep the program running until user exits
while True:
    print("\nOptions: 1. Add Task  2. Remove Task  3. View Task  4. Exit")

    # Ask user for their choice
    choice = input("Enter your choice:")

    if choice == '1':
        task = input("Enter task to Add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to Remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting program....")
        break
    else:
        print("Invalid Choice! Please check again")
        
