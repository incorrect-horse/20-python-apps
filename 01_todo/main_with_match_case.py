todo_list = 'files/todos.txt'

while True:
#    usr_actn = input("\nTODO LIST -- Type add, show, edit, complete, or exit: ")
#    usr_actn = input("\nTODO LIST -- Type add [a], show [s], edit [e], complete [c], or exit [x]: ")
    usr_actn = input("\nTODO LIST -- Type add | a, show | s, edit | e, complete | c, or exit | x: ")
    usr_actn = usr_actn.strip().lower()

    match usr_actn:
        case 'add' | 'a':
            todo = input("\nEnter a todo: ") + "\n"

            with open(todo_list, 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open(todo_list, 'w') as file:
                file.writelines(todos)
        case 'show' | 's':
            with open(todo_list, 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1} - {item.title()}")
        case 'edit' | 'e':
            item_no = int(input("\nWhich task number do you want to edit? "))
            item_no -= 1

            with open(todo_list, 'r') as file:
                todos = file.readlines()

            new_item = input("\nEnter a new task: ")
            todos[item_no] = new_item + "\n"

            with open(todo_list, 'w') as file:
                file.writelines(todos)
        case 'complete' | 'c':
            comp_no = int(input("\nEnter a task number to complete: "))
            comp_no -= 1

            with open(todo_list, 'r') as file:
                todos = file.readlines()

            comp_task = todos[(comp_no)].strip("\n")
            todos.pop(comp_no)

            with open(todo_list, 'w') as file:
                file.writelines(todos)

            print("\nTask '" + comp_task.upper() + "' was removed from todo list.")
        case 'exit' | 'x':
            break
        case unknown:
            print("\nCommand not recognized...  Try again.")

print("\nBye-bye!\n")
 