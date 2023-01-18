import colorama
from colorama import Fore


def get_todos(filepath="todos-1.txt"):
    """
    Read a text file and return the list of Todo items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos-1.txt"):
    """ Write Todo item in the text file """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input(Fore.LIGHTBLUE_EX + "Type add, show, edit, complete, or exit : ").strip()

    if user_action.startswith('add'):
        todo = "\n" + user_action[4:]
        todos = get_todos()
        todos.append(todo)
        """ 
        write_todos(todos, "todos-1.txt") 
        "todos-1.txt" is a default argument so we ignore writing it here in the braces.
        """
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        print(Fore.MAGENTA + "Yor list of To-dos : ")
        for i, item in enumerate(todos, 1):
            print(Fore.LIGHTYELLOW_EX + f"{i}" + '. ' + item.title().strip("\n"))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = get_todos()
            input_replace = input(Fore.LIGHTCYAN_EX + "Enter Todo to replace : ")
            todos[int(number) - 1] = input_replace + "\n"
            write_todos(todos)
        except ValueError:
            print(Fore.LIGHTRED_EX + "Your Command is not Valid!!")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
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

