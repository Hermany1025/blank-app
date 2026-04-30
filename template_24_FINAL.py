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
    st.subheader("Welcome to Hermany's AI Judge Template_24_Final")
    Name = st.text_input("Your Legal Name", key="name")
    ID = st.text_input("ID")