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
dictionary = {}
Add = st.button("Add new defendants")
Search = st.button("Search through Name or ID")
if Add:
    with st.form("Form"):
        st.title("Welcome to Hermany's AI Judge Template_24_Final")
        Name = st.text_input("Your Legal Name", key="name")
        ID = st.text_input("ID")
        st.subheader("Current Sentence Need to be Served")
        col1, col2 = st.columns(2)
        with col1:
            Penalties = st.radio("Penalties", ["Nothing(Cannot be Served)", "Death Penalty", "Death Reprieve","Life Imprisonment", "Year Imprisonment"])
        
        with col2:
            Year = st.number_input("Year", min_value=0.0, max_value = 10000.0, step = 0.5, value = 0.0)
        Case = st.text_area("Case Details", key="details")
        Submit = st.form_submit_button("Submit")    
    if Submit:
        if Name == "" or ID == "" or Case == "" or not (Penalties == "Nothing(Cannot be Served)" and Year > 0.0):
            st.error("Please fill in all the required fields.")
        else:
            st.success("Thanks for submission, Hermany will judge your case as soon as possible. Please wait patiently.")
            rule_prompt = '''
            a. You are fair
            b. You are impartial
            c. Even though you are helping the defendants, you cannot take pity or pleading. Or lean on the defendants to be purposely decreasing the sentence.
            d. Be FAIR
            e. BE IMPARTICAL
            f. NO PITY
            g. NO PLEADING
            '''
            Example = '''
            {
                Result:{
                },
                Why do you have the result:{
                }

            }
            '''
            user_prompt = f'''
            You are a professional AI Judge. You will help those appeal defendants. But please strictly follow the rule, {rule_prompt}. The defendant's name is {Name}, and ID is {ID}. Based on the defendants current sentence {Year} or {Penalties} and {Case}.
            STRICTLY USE THE FORMAT OF {Example}.
            '''
            response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "user", "content": user_prompt}
                        ]
                    )
            # st.write(response.choices[0].message.content)
            # st.write("\n\n",response.choices[0].message.content)
            Output = json.loads(response.choices[0].message.content)
            # st.write(st.session_state.output)
            Output[Name] = Output
            dictionary = Output
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Result")
                st.write(Output["Result"])
            with col2:
                st.subheader("Why do you have the result")
                st.write(Output["Why do you have the result"])
if Search:
    if len(Output) == 0:
            st.error("There is no wrongly convicted case in the database, please add new defendants to the database.")
    else:
        search_query = st.text_input("Search by Name or ID")
        if search_query:
            if search_query in Output:
                st.subheader("Result")
                st.write(Output[search_query]["Result"])
                st.subheader("Why do you have the result")
                st.write(Output[search_query]["Why do you have the result"])
            else:
                st.error("No results found for the given Name or ID.")