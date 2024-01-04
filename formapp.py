import streamlit as st
import pandas as pd
def open_page():
    with st.form("open_form"):
        x1=st.text_input("Enter the number-1 ",value=0)
        y2=st.text_input("Enter the number-2",value=0)
        sub=st.form_submit_button("Ok")
        
st.header("Sample Form")
with st.form("my_form"):
    x=st.text_input("Enter the number-1 ",value=0)
    y=st.text_input("Enter the number-2",value=0)
    st.checkbox("Male")
    st.checkbox("Female")
    color=st.color_picker("Select Color")
    #st.write(x)
    submit=st.form_submit_button("submit")
    if submit:
        st.write("Addition is ",int(x)+int(y))
        st.write("Selected Color is ",color)
        st.sidebar.title("Navigation")
        

df=pd.read_csv("sonar_data.csv")
st.write(df.head())
