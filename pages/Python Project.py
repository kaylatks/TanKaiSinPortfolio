import streamlit as st
import subprocess

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

# st.write(f"""
# 3. Two Sums
#     - This function is used to find the index of sum up value
#     eg: list: [1,4,8]
#         target: 9
#         index of sum up value: [0,2]
#
# **Tip for play**
#
# i.   Enter the list number seperated by spaces
#      eg: 1 4 8
#
# ii.  Enter target value, a number to total up
#      eg: 9
#
# iii. display the result, the index of 1 and 8
# """)
#
#
# command = subprocess.call(['python', 'TwoSums.py'])
# # Create a clickable link using HTML
# link = f'<a href="#" onclick="window.open(\'data:application/octet-stream,{command}\');">Two Sums</a>'
#
# # Display the clickable link in Streamlit
# st.markdown(link, unsafe_allow_html=True)
