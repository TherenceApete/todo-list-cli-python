import os
from datetime import datetime
print("Welcome to your To-Do List App!\n")

def add_task(filename, task):
    with open(filename, "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(task + " | " + time + "\n")

def view_tasks(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines.sort()
        for i, line in enumerate(lines):
            print(str(i+1) + ". " + line)
        print("Total Task: " + str(len(lines)))

def delete_task(filename, line_index_to_delete):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines.sort()
    if line_index_to_delete > len(lines) or line_index_to_delete <= 0 :
        print("Invalid task number")
    else:
        with open(filename, "w") as file:
            for i, line in enumerate(lines):
                if i != line_index_to_delete - 1:
                    file.write(line)
        print("Task deleted!")
program_open = True
filename = "task.txt"

if not os.path.exists(filename):
    open(filename, 'w').close()

while program_open:
    command = input("Enter a command (add/view/delete/exit): ")

    if command.lower() == "add":
        task = input("Enter a task: ")
        add_task(filename, task)
        print("Task added!")

    elif command.lower() == "view":
        view_tasks(filename)

    elif command.lower() == "delete":

        index = int(input("Which task number to delete ? "))
        delete = input(f"Are you sure you want to delete task {index} ?(Y/N)")
        if delete.upper() == "Y":
            delete_task(filename, index)

    elif command.lower() == "exit":
        program_open = False
        print("Goodbye")

    else:
        print("The command entered does not exist, please try again")




