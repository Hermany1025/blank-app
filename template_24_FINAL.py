# 1
import streamlit as st
import json
from openai import OpenAI

# 2

st.title("Hermany's Pokemon Gernater")
st.subheader("Template_24_Final")
st.write("All Copywrite belonged to Hermany, Chinmany Seimens complany. https://Chinmany_Seimens/Hermanys_AI_Judge_template_24_Final.cn.com")
st.divider()
client = OpenAI(
    api_key = st.secrets["OPENAIKEY"]
)

with st.form("Form"):
    st.title("Welcome to Hermany's AI Judge Template_24_Final")
    Name = st.text_input("Your Legal Name", key="name")
    ID = st.text_input("ID")
    st.subheader("Current Sentence Need to be Served")
    col1, col2 = st.columns(2)
    with col1:
        Penalties = st.radio("Penalties", ["Nothing(Cannot be Served)", "Death Penalty", "Death Reprieve","Life Imprisonment"])
    
    with col2:
        Year = st.number_input("Year", min_value=0.0, max_value = 1000.0, step = 0.5, value = 0.0)
    Case = st.text_area("Case Details", key="details")
    Submit = st.form_submit_button("Submit")    
if Submit:
    if Name == "" or ID == "" or Year == 0.0 or Case == "" or Penalties == "Nothing(Cannot be Served)":
        st.error("Please fill in all the required fields.")
    else:
        st.success("Thanks for submission, Hermany will judge your case as soon as possible. Please wait patiently.")

