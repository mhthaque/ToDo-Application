import colorama
from colorama import Fore
import csv

with open("files/address.csv", "r") as file:
    data = list(csv.reader(file))

print(Fore.LIGHTRED_EX + f"{data}")

state = input("Enter state name : ")
for row in data:
    if row[4] == state:
        print(row[0] + " " + row[1])