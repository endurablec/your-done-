!pip install -q streamlit

!npm install localtunnel

%%writefile app.py 

import streamlit as st

st.title("Welcome to My First Streamlit App")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to the app.")
!streamlit run app.py &>/content/logs.txt &