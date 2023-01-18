import functions
import colorama
from colorama import Fore
import PySimpleGUI as sg

label = sg.Text("Type your To-Do Here : ", text_color='white')
input_box = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")
window = sg.Window("BelovedHorizon To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()

