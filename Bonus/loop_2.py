import colorama
from colorama import Fore

while True:
    user_action = input(Fore.LIGHTBLUE_EX + "Type add, show, edit, delete, or exit : ").lower().strip().replace(" ", "")
    match user_action:
        case 'add':
            todo = input(Fore.LIGHTYELLOW_EX + "Type your To-do : ") + "\n"
            file = open('../Todo-app/todos-1.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('../Todo-app/todos-1.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            file = open('../Todo-app/todos-1.txt', 'r')
            todos = file.readlines()
            file.close()

            print(Fore.MAGENTA + "Yor list of To-dos : ")

            for i, item in enumerate(todos, 1):
                print(Fore.LIGHTYELLOW_EX + f"{i}" + '. ' + item.title().strip("\n"))
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

