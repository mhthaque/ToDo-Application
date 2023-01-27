import colorama
from colorama import Fore

while True:
    user_action = input(Fore.LIGHTBLUE_EX + "Type add, show, edit, delete, or exit : ").strip()

    if user_action.startswith('add'):
        todo = "\n" + user_action[3:]
        with open('../Todo-app/todos-1.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)
        with open('../Todo-app/todos-1.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open('../Todo-app/todos-1.txt', 'r') as file:
            todos = file.readlines()
        print(Fore.MAGENTA + "Yor list of To-dos : ")
        for i, item in enumerate(todos, 1):
            print(Fore.LIGHTYELLOW_EX + f"{i}" + '. ' + item.title().strip("\n"))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            with open("../Todo-app/todos-1.txt", "r") as file:
                todos = file.readlines()
            input_replace = input(Fore.LIGHTCYAN_EX + "Enter Todo to replace : ")
            todos[int(number) - 1] = input_replace + "\n"
            with open("../Todo-app/todos-1.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print(Fore.LIGHTRED_EX + "Your Command is not Valid!!")
            continue

    elif user_action.startswith('delete'):
        user_input = int(input(Fore.GREEN + "What item do you want to delete? press 1/2/3 .. : "))
        todos.pop(user_input - 1)

    elif user_action.startswith('exit'):
        break

    elif '_' in user_action:
        print(Fore.LIGHTBLUE_EX + "You've entered unknown option. Type again .. :")
    else:
        print(Fore.LIGHTRED_EX + "Your command is not valid. Enter yoyr command again")
print()
print('Bye!')

