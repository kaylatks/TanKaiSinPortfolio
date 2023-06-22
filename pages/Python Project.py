import streamlit as st


st.info("All the below project are using python code to build. Kindly give a hand to play and test!!!")

st.write(f"""
1. Portfolio
    - Portfolio build with python
""")
# URL of the Streamlit app you want to link to
app_url1 = "https://kaylatks-tankaisinportfolio-home-3p7r4o.streamlit.app/"

# Generate an HTML link
link_html1 = f'<a href="{app_url1}" target="_blank">Kai Sin Portfolio</a>'

# Display the link
st.components.v1.html(link_html1, height=30)


st.write(f"""
2. Todo App
    - It is a to do list, user can use it to record and plan what will do.

**Tip for play**

i.  Add a new todo in text box and press enter, it will display in the list

ii. Tick the checkbox to remove any item from the list

""")

# URL of the Streamlit app you want to link to
app_url2 = "https://kaylatks-my-todo-app-web-d4wsvh.streamlit.app/"

# Generate an HTML link
link_html2 = f'<a href="{app_url2}" target="_blank">ToDo App</a>'

# Display the link
st.components.v1.html(link_html2, height=30)