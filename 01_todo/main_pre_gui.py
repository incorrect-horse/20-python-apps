from functions import get_todo_list, write_todo_list
import time

todo_list = 'files/todos.txt'
now = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"\nThe current date and time is: {now}")

while True:
    #usr_actn = input("\nTODO LIST -- Type add, show, edit #, complete #, or exit: ")
    usr_actn = input("\nTODO LIST -- Type a | add, s | show, e | edit, c | complete, or x | exit: ")
    usr_actn = usr_actn.strip().lower()

    #if usr_actn.startswith('add'):
    if usr_actn.startswith('add') or usr_actn.startswith('a'):
        #todo = usr_actn[4:]
        todo = usr_actn.split(" ", 1)[1]

        todos = get_todo_list(todo_list)

        todos.append(todo + '\n')

        write_todo_list(todos)

    #elif usr_actn.startswith('show'):
    elif usr_actn.startswith('show') or usr_actn.startswith('s'):
        todos = get_todo_list(todo_list)

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} - {item.capitalize()}")

    #elif usr_actn.startswith('edit'):
    elif usr_actn.startswith('edit') or usr_actn.startswith('e'):
        try:
            #task_no = int(usr_actn[5:])
            task_no = int(usr_actn.split(" ", 1)[1])
            task_no -= 1

            todos = get_todo_list(todo_list)
            new_item = input("\nEnter a new task: ")
            todos[task_no] = new_item + "\n"
            write_todo_list(todo_list, todos)

        except ValueError:
            print("Command is not valid.")
            continue

    #elif usr_actn.startswith('complete'):
    elif usr_actn.startswith('complete') or usr_actn.startswith('c'):
        try:
            #comp_no = int(usr_actn[9:])
            comp_no = int(usr_actn.split(" ", 1)[1])
            comp_no -= 1

            todos = get_todo_list(todo_list)

            while comp_no >= len(todos):
                print(f"\nThe number you entered, {comp_no + 1}, is not in the list's range.")
                comp_no = int(input(f"\nPlease enter a task number between 1 and {len(todos)}: "))
                comp_no -= 1
            comp_task = todos[(comp_no)].strip("\n")

            todos.pop(comp_no)
            write_todo_list(todo_list, todos)

            print("\nTask '" + comp_task.upper() + "' was removed from todo list.")
        except:
            print("There is no item with that number.")
            continue

    #elif usr_actn.startswith('exit'):
    elif usr_actn.startswith('exit') or usr_actn.startswith('x'):
        break

    else:
        print("\nOops! Command not recognized...  Try again.")

print("\nBye-bye!\n")
