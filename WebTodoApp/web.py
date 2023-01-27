import streamlit as ST
from functions import get_todos

todos = get_todos()

ST.title("My WebTodo App")
ST.subheader("This is my todo app.")
ST.write("This app is to increase your productivity.")


for todo in todos:
    ST.checkbox(todo)



