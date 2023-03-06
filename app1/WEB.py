import streamlit as st
import functions

todos = functions.get_todos()

st.title("To-Do App")
st.subheader("To increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new to-do!")