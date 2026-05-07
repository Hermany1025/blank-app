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
if "Output" not in st.session_state:
    st.session_state.Output = {}
if "dictionary" not in st.session_state:
    st.session_state.dictionary = {}
if "btn1" not in st.session_state:
    st.session_state.btn1 = ""
if "btn2" not in st.session_state:
    st.session_state.btn2 = ""
if "Name" not in st.session_state:
    st.session_state.Name = ""
if "ID" not in st.session_state:
    st.session_state.ID = ""
if "Penalties" not in st.session_state:
    st.session_state.Penalties = ""
if "Year" not in st.session_state:
    st.session_state.Year = 0.0
if "Case" not in st.session_state:
    st.session_state.Case = ""
if "Submit" not in st.session_state:
    st.session_state.Submit = False
if "search_query" not in st.session_state:
    st.session_state.search_query = ""
if "response" not in st.session_state:
    st.session_state.response = ""
if "rule_prompt" not in st.session_state:
    st.session_state.rule_prompt = '''
            a. You are fair
            b. You are impartial
            c. Even though you are helping the defendants, you cannot take pity or pleading. Or lean on the defendants to be purposely decreasing the sentence.
            d. Be FAIR
            e. BE IMPARTICAL
            f. NO PITY
            g. NO PLEADING
            '''
if "Example" not in st.session_state:
    st.session_state.Example = '''
            {
                Result:{
                },
                Why do you have the result:{
                }

            }
            '''
if "user_prompt" not in st.session_state:
    st.session_state.user_prompt = f'''
            You are a professional AI Judge. You will help those appeal defendants. But please strictly follow the rule, {st.session_state.rule_prompt}. The defendant's name is {st.session_state.Name}, and ID is {st.session_state.ID}. Based on the defendants current sentence {st.session_state.Year} or {st.session_state.Penalties} and {st.session_state.Case}.
            STRICTLY USE THE FORMAT OF {st.session_state.Example}.
            '''

dictionary = {}


with st.sidebar:
    st.header("Pages")
    if st.button("Add New Defendant", use_container_width=True):
        st.session_state.btn1 = "Add New Defendant"
    if st.button("Search by Name or ID", use_container_width=True):
        st.session_state.btn2 = "Search by Name or ID"
if st.session_state.btn1 == "Add New Defendant":
    with st.form("Form"):
        st.title("Welcome to Hermany's AI Judge Template_24_Final")
        st.session_state.Name = st.text_input("Your Legal Name", key="name")
        st.session_state.ID = st.text_input("ID")
        st.subheader("Current Sentence Need to be Served")
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.Penalties = st.radio("Penalties", ["Nothing(Cannot be Served)", "Death Penalty", "Death Reprieve","Life Imprisonment", "Year Imprisonment"])
        
        with col2:
            st.session_state.Year = st.number_input("Year", min_value=0.0, max_value = 10000.0, step = 0.5, value = 0.0)
        st.session_state.Case = st.text_area("Case Details If searching for a specific case type", key="details")
        st.session_state.Submit = st.form_submit_button("Submit")    
    if st.session_state.Submit:
        st.write("Hitler is coming, Hermany is judging your case, please wait patiently.")
        if st.session_state.Name == "" or st.session_state.ID == "" or st.session_state.Case == "" or not (st.session_state.Penalties == "Year Imprisonment" and st.session_state.Year > 0.0):
            st.error("Please fill in all the required fields.")
        else:
            st.success("Thanks for submission, Hermany will judge your case as soon as possible. Please wait patiently.")
            st.session_state.rule_prompt = '''
            a. You are fair
            b. You are impartial
            c. Even though you are helping the defendants, you cannot take pity or pleading. Or lean on the defendants to be purposely decreasing the sentence.
            d. Be FAIR
            e. BE IMPARTICAL
            f. NO PITY
            g. NO PLEADING
            '''
            st.session_state.Example = '''
            {
                Result:{
                },
                Why do you have the result:{
                }

            }
            '''
            st.session_state.user_prompt = f'''
            You are a professional AI Judge. You will help those appeal defendants. But please strictly follow the rule, {st.session_state.rule_prompt}. The defendant's name is {st.session_state.Name}, and ID is {st.session_state.ID}. Based on the defendants current sentence {st.session_state.Year} or {st.session_state.Penalties} and {st.session_state.Case}.
            STRICTLY USE THE FORMAT OF {st.session_state.Example}.
            '''
            st.session_state.response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "user", "content": st.session_state.user_prompt}
                        ]
                    )
            st.write(st.session_state.response.choices[0].message.content)
            st.write("\n\n",st.session_state.response.choices[0].message.content)
            st.session_state.Output = json.loads(st.session_state.response.choices[0].message.content)
            st.session_state.Output[st.session_state.Name] = st.session_state.Output
            st.session_state.dictionary = st.session_state.Output
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Why do you have the result")
                st.write(st.session_state.Output["Why do you have the result"])
            with col2:
                st.subheader("Result")
                st.write(st.session_state.Output["Result"])
    st.write(st.session_state.Output)
if st.session_state.btn2 == "Search by Name or ID":
    if len(st.session_state.Output) == 0:
        st.error("There is no wrongly convicted case in the database, please add new defendants to the database.")
    else:
        st.session_state.search_query = st.text_input("Search by Name or ID")
        if st.session_state.search_query:
            if st.session_state.search_query in st.session_state.Output:
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Why do you have the result")
                    st.write(st.session_state.Output ["Why do you have the result"])
                with col2:
                    st.subheader("Result")
                    st.write(st.session_state.Output[st.session_state.search_query]["Result"])
            else:
                st.error("No results found for the given Name or ID.")