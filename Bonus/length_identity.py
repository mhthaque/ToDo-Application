import colorama
from colorama import Fore

password = input(Fore.LIGHTRED_EX + "Enter Your Password : ")

while password != 'P@ssw0rd123!':
    print("XX You've typed an incorrect password. Type your password again")
    password = input(Fore.LIGHTRED_EX + "Enter Your Password : ")

print("Password is CORRECT!! You're logged in!!")




