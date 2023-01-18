import colorama
from colorama import Fore


def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input(Fore.LIGHTBLUE_EX + "Type add, show, edit, complete, or exit : ").strip()

    if user_action.startswith('add'):
        todo = "\n" + user_action[3:]
        todos = get_todos('../todos-1.txt')
        todos.append(todo)
        write_todos("../todos-1.txt", todos)

    elif user_action.startswith('show'):
        todos = get_todos("../todos-1.txt")
        print(Fore.MAGENTA + "Yor list of To-dos : ")
        for i, item in enumerate(todos, 1):
            print(Fore.LIGHTYELLOW_EX + f"{i}" + '. ' + item.title().strip("\n"))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = get_todos('../todos-1.txt')
            input_replace = input(Fore.LIGHTCYAN_EX + "Enter Todo to replace : ")
            todos[int(number) - 1] = input_replace + "\n"
            write_todos("../todos-1.txt", todos)
        except ValueError:
            print(Fore.LIGHTRED_EX + "Your Command is not Valid!!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos("../todos-1.txt")
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos("../todos-1.txt", todos)
            message = f"Todo {todo_to_remove} was removed from the list. "
            print(message)
        except ValueError:
            print(Fore.LIGHTRED_EX + "There is not any item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    elif '_' in user_action:
        print(Fore.LIGHTBLUE_EX + "You've entered unknown option. Type again .. :")
    else:
        print(Fore.LIGHTRED_EX + "Your command is not valid. Enter yoyr command again")
print()
print('Bye!')

