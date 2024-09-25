""" Execute script in terminal (streamlit run [filename].py) to render and launch webpage """
import streamlit as st
import functions

todo_list = functions.get_todo_list()


def add_task():
    new_task = st.session_state["new_task"] + '\n'
    todo_list.append(new_task)
    functions.write_todo_list(new_task, write_state='a')


st.title("My Todo crApp")
st.subheader("This is my super buggy Todo Checklist app...")
st.write("No, not <b>bugs</b>, they're <u>features!!</u>", unsafe_allow_html=True)

st.text_input(label="Add a new task.", placeholder="enter new tasks here...",
              on_change=add_task, key="new_task")

for index, task in enumerate(todo_list):
    checkbox = st.checkbox(task, key=index)
    #print(index, task)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo_list(todo_list)
        del st.session_state[index]
        st.experimental_rerun()

#print("script executed")
#st.session_state
