import colorama
from colorama import Fore
print(Fore.LIGHTRED_EX + 'Enter a To-Do Item: ')
input_collect = input(Fore.CYAN + 'Enter your choice (SHOW | ADD | DELETE | UPDATE) : ')
print(Fore.LIGHTYELLOW_EX + f'You have typed your response : {input_collect}')
todo1 = input(Fore.LIGHTBLUE_EX + "Type your 1st item response : ")
todo2 = input(Fore.LIGHTBLUE_EX + "Type your 2nd item response : ")
todo3 = input(Fore.LIGHTBLUE_EX + "Type your 3rd item response : ")
todos = [todo1, todo2, todo3]
print()

for i, item in enumerate(todos,1):
    print(i, '. ' + item, end='\n')

