"""
This code will find all text file within a given directory
"""
import colorama
from colorama import Fore

import glob
result = glob.glob("files/*.txt")


print(Fore.LIGHTGREEN_EX + "The search result : ")
print(Fore.LIGHTMAGENTA_EX + f"{result}")
print('\n' + Fore.LIGHTRED_EX + "The Content of the txt files are : \n")


for filepath in result:
    with open(filepath, 'r') as file:
        print(Fore.LIGHTBLUE_EX + file.read())
