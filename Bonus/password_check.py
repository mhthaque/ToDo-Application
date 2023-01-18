import colorama
from colorama import Fore
password = input(Fore.LIGHTMAGENTA_EX + "Enter Your Password : ")
print(Fore.LIGHTYELLOW_EX + f"Your Password is : {password}")


result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for item in password:
    if item.isdigit():
        digit = True
result["digits"] = digit

uppercase = False
for item in password:
    if item.isupper():
        uppercase = True
result["upper-case"] = uppercase

print(result)

if all(result) == True:
    print(Fore.LIGHTBLUE_EX + "You've typed a STRONG password :D")
else:
    print(Fore.LIGHTRED_EX + "You've typed a WEAK password :(")





