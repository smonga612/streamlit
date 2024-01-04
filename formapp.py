import streamlit as st
with st.form("my_form"):
    x=st.text_input("Enter the number-1 ",value=0)
    y=st.text_input("Enter the number-2",value=0)
    st.checkbox("Male")
    st.checkbox("Female")
    color=st.color_picker("Select Color")
    #st.write(x)
    submit=st.form_submit_button()
    if submit:
        st.write("Addition is ",int(x)+int(y))
        st.write("Selected Color is ",color)
