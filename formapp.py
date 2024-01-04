import streamlit as st
with st.form("my_form"):
    x=st.text_input("Enter the number-1 ")
    y=st.text_input("Enter the number-2")
    #st.write(x)
    submit=st.form_submit_button()
    if submit:
        st.write("Addition is ",int(x)+int(y))
