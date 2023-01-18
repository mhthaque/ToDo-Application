import colorama
from colorama import Fore

while True:
    user_action = input(Fore.LIGHTBLUE_EX + "Type add, show, edit, delete, or exit : ").lower().strip().replace(" ", "")
    match user_action:

        case 'add':
            todo = input(Fore.LIGHTYELLOW_EX + "Type your To-do : ") + "\n"
            with open('../todos-1.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)
            with open('../todos-1.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('../todos-1.txt', 'r') as file:
                todos = file.readlines()
            print(Fore.MAGENTA + "Yor list of To-dos : ")
            for i, item in enumerate(todos, 1):
                print(Fore.LIGHTYELLOW_EX + f"{i}" + '. ' + item.title().strip("\n"))

        case 'edit':
            input_edit = int(input(Fore.LIGHTMAGENTA_EX + "Enter the number of the Todo to edit : "))
            input_replace = input("Type Your change : ")
            with open("../todos-1.txt", "r") as file:
                todos = file.readlines()
            todos[input_edit - 1] = input_replace + "\n"
            with open("../todos-1.txt", "w") as file:
                file.writelines(todos)


        case 'delete':
            user_input = int(input(Fore.GREEN + "What item do you want to delete? press 1/2/3 .. : "))
            todos.pop(user_input - 1)

        case 'exit':
            break

        case _:
            print(Fore.LIGHTBLUE_EX + "You've entered unknown option. Type again .. :")

print()
print('Bye!')

