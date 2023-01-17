import webbrowser
from colorama import Fore

search_keyword = input("Type your search keyword : ")

webbrowser.open("https://www.google.com/search?q=" + search_keyword)
