import functions
import PySimpleGUI as psg
import time
import os

SUBDIR = 'files'
TASKLIST = 'todos.txt'
FILEPATH = SUBDIR + "/" + TASKLIST

if not os.path.exists(SUBDIR):
    os.mkdir(SUBDIR)

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass

#psg.theme("DarkGrey12")
task_theme = psg.theme("Dark")
#psg.theme("Black")

clock = psg.Text("", key="clock")
label = psg.Text("Enter a new task")
input_box = psg.InputText(tooltip="Enter a task",
                          key="new_task",
                          size=[40, 1])
add_button = psg.Button("Add")
#add_button = psg.Button(size=2,
#                        image_source="files/add.png",
#                        mouseover_colors="LightBlue2",
#                        tooltip="Add task",
#                        key="Add")
list_box = psg.Listbox(values=functions.get_todo_list(),
                       key="todo_list",
                       enable_events=True,
                       size=[45, 10])
edit_button = psg.Button("Edit", size=9)
comp_button = psg.Button("Complete", size=9)
exit_button = psg.Button("Exit")

l_col_cont = [[clock],
             [label],
             [add_button, input_box],
             [list_box],
             [exit_button]]

r_col_cont = [[edit_button],
             [comp_button]]

left_col = psg.Column(l_col_cont)
right_col = psg.Column(r_col_cont)

layout = [[left_col, right_col]]

window = psg.Window(
    'My To-Do App',
        layout,
        font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=200)
    event, values = window.read()
    window['clock'].update(value=time.strftime("%b %d %Y, %H:%M:%S"))
    #print(1, event)
    #print(2, values)
    #print(3, values['todo_list'])
    match event:
        case "Add":
            if values['new_task'].strip() == "":
                psg.popup("Please input a task to add.",
                          font=('Helvetica', 15))
            else:
                todo_list = functions.get_todo_list()
                new_todo = values['new_task'].strip().capitalize() + "\n"
                todo_list.append(new_todo)
                functions.write_todo_list(todo_list)
                window['todo_list'].update(values=todo_list)
        case "Edit":
            try:
                edit_task = values['todo_list'][0]
                new_task = values['new_task']
                todo_list = functions.get_todo_list()
                index = todo_list.index(edit_task)
                todo_list[index] = new_task + "\n"
                functions.write_todo_list(todo_list)
                window['todo_list'].update(values=todo_list)
            except IndexError:
                psg.popup("Please select a task first.",
                          font=('Helvetica', 15))
        case "Complete":
            try:
                comp_task = values['todo_list'][0]
                comp_todos = functions.get_todo_list()
                comp_todos.remove(comp_task)
                functions.write_todo_list(comp_todos)
                window['todo_list'].update(values=comp_todos)
                window['new_task'].update(value="")
            except IndexError:
                psg.popup("Please select a task first.",
                          font=('Helvetica', 15))
        case "Exit":
            break
        case "todo_list":
            try:
                window['new_task'].update(value=values["todo_list"][0].strip('\n'))
            except IndexError:
                psg.popup("Type a new task and click Add to get started.",
                          font=('Helvetica', 15))
        case psg.WIN_CLOSED:
            break

window.close()
