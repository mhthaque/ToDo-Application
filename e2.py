import colorama
from colorama import Fore
import json

with open('Test/questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    # print(question["alternatives"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}" + ". " + f"{alternative}")
    user_choice = int(input("Enter your choice (NumbersOnly) : "))
    question["user_choice"] = user_choice

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer! "
    else:
        result = "Wrong Answer! "

    message = Fore.LIGHTGREEN_EX  + f"{index+1}. " + f"{result}- " + Fore.LIGHTGREEN_EX + f"Your answer: {question['user_choice']} " + " " + \
              f"| Correct answer: {question['correct_answer']}" + " -> " + f"{question['alternatives']}"

    print(message)

print()
print(Fore.LIGHTCYAN_EX + "Your ultimate score is : ")
print(score, "/", len(data))
