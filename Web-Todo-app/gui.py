import functions
import time
import PySimpleGUI as PSG
PSG.theme('DarkTeal2')

clock = PSG.Text("", key="clock")
label = PSG.Text("Type your To-Do Here : ", text_color='white')
input_box = PSG.InputText(tooltip="Enter To-Do", key="todo", size=[64, 20])
add_button = PSG.Button("Add", size=10)
list_box = PSG.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[62, 11])
edit_button = PSG.Button("Edit")
complete_button = PSG.Button('Complete')
exit_button = PSG.Button("Exit")

"""
  window = sg.Window("BelovedHorizon To-Do App", layout=[[label], [input_box, add_button]])
  window = sg.Window("BelovedHorizon To-Do App", layout=[[label], [input_box], [add_button]])
"""
window = PSG.Window("BelovedHorizon To-Do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Font Awesome', 15))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %y %H:%M:%S"))
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
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                todos = functions.get_todos()
            except IndexError:
                PSG.popup("Please select an item from the list first!", font=('Font Awesome', 14))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                PSG.popup("Please select an item from the list first!", font=('Font Awesome', 14))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case PSG.WINDOW_CLOSED:
            break

window.close()
