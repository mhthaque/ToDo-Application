import colorama
from colorama import Fore

todos = []

while True:
    user_action = input(Fore.LIGHTBLUE_EX + "Type add, show, edit, delete, or exit : ").lower().strip().replace(" ", "")
    match user_action:
        case 'add':
            todo = input(Fore.LIGHTYELLOW_EX + "Type your To-do : ") + "\n"
            todos.append(todo)
            file = open('todos.txt', 'a')
            file.writelines(todos)
        case 'show' | 'display':
            print(Fore.MAGENTA + f"Yor list of To-dos : {todo}")
            for i, item in enumerate(todos, 1):
                print(Fore.LIGHTRED_EX + f"{i}" + '. ' + item.title(), end="\n")
        case 'edit':
            input_edit = int(input(Fore.LIGHTMAGENTA_EX + "Enter the number of the Todo to edit : "))
            input_replace = input("Type Your change : ")
            todos[input_edit - 1] = input_replace
        case 'delete':
            user_input = int(input(Fore.GREEN + "What item do you want to delete? press 1/2/3 .. : "))
            todos.pop(user_input - 1)
        case 'exit':
            break
        case _:
            print(Fore.LIGHTBLUE_EX + "You've entered unknown option. Type again .. :")

print()
print('Bye!')

