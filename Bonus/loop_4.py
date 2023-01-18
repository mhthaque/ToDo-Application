import colorama
from colorama import Fore

while True:
    user_action = input(Fore.LIGHTBLUE_EX + "Type add, show, edit, delete, or exit : ").strip()

    if 'add' in user_action:
        todo = "\n" + user_action[3:]
        with open('../todos-1.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)
        with open('../todos-1.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('../todos-1.txt', 'r') as file:
            todos = file.readlines()
        print(Fore.MAGENTA + "Yor list of To-dos : ")
        for i, item in enumerate(todos, 1):
            print(Fore.LIGHTYELLOW_EX + f"{i}" + '. ' + item.title().strip("\n"))

    elif 'edit' in user_action:
        input_replace = input(Fore.LIGHTCYAN_EX + "Enter Todo to replace : ")
        number = user_action[5:]
        with open("../todos-1.txt", "r") as file:
            todos = file.readlines()
        todos[int(number) - 1] = input_replace + "\n"
        with open("../todos-1.txt", "w") as file:
            file.writelines(todos)

    elif 'delete' in user_action:
        user_input = int(input(Fore.GREEN + "What item do you want to delete? press 1/2/3 .. : "))
        todos.pop(user_input - 1)

    elif 'exit' in user_action:
        break

    elif '_' in user_action:
        print(Fore.LIGHTBLUE_EX + "You've entered unknown option. Type again .. :")
    else:
        print(Fore.LIGHTRED_EX + "Your command is not valid. Enter yoyr command again")
print()
print('Bye!')

