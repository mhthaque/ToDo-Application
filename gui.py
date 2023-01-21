import functions
import colorama
from colorama import Fore
import PySimpleGUI as PSG
PSG.theme('DarkTeal2')

label = PSG.Text("Type your To-Do Here : ", text_color='white')
input_box = PSG.InputText(tooltip="Enter To-Do", key="todo", size=[64, 20])
add_button = PSG.Button("Add")
list_box = PSG.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[62, 11])
edit_button = PSG.Button("Edit")


"""
  window = sg.Window("BelovedHorizon To-Do App", layout=[[label], [input_box, add_button]])
  window = sg.Window("BelovedHorizon To-Do App", layout=[[label], [input_box], [add_button]])
"""
window = PSG.Window("BelovedHorizon To-Do App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case 'Edit':
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)

            todos = functions.get_todos()
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case PSG.WINDOW_CLOSED:
            break

window.close()
