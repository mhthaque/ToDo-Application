import streamlit as ST
import functions

todos = functions.get_todos()

ST.title("My WebTodo App")
ST.subheader("This is my todo app.")
ST.write("This app is to increase your productivity.")


for todo in todos:
    ST.checkbox(todo)

ST.text_input(label="", placeholder="Enter a Todo")





