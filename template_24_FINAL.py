# 1
import streamlit as st
import json
import st_yled
from openai import OpenAI

st_yled.init()
# 2
# GLOBAL CONTAINER
PRIMARY = "#E42121"
SECONDARY = "#3567FF"
TERTIARY= "#FFF700"
QUATERNARY= "#FF9500"
GRAY = "#535353"
GREEN = "#E4F6B3"
st_yled.set("button", "background_color", GREEN)
st_yled.set("form_submit_button", "background_color", GREEN)
st_yled.set("write", "font_size", "20px")


with st_yled.container(
    background_color = GREEN,
    border_color = "#E4F6B3",
    padding = "20px"
):
    st_yled.title("Hermany's AI Judge")
    st_yled.subheader("Template_24_Final")
    st_yled.write("All Copywrite belonged to Hermany, Chinmany Seimens complany. https://Chinmany_Seimens/Hermanys_AI_Judge_template_24_Final.cn.com")
st.divider()
client = OpenAI(
    api_key = st.secrets["OPENAIKEY"]
)

# 3 session state
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False
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
            e. BE IMPARTIAL
            f. NO PITY
            g. NO PLEADING
            h. If the defendants that was not wrongly convicted and have worse cases than should be punishes, like Cases> Punishments. You are able to add punishments to that denfendants.
            i. Give out the correct result.
                Like years, or what punishments
            '''

if "Example" not in st.session_state:
    st.session_state.Example = '''
            {
                "Result": "Write the result here",
                "Why do you have the result": "Write the reason here"
            }
            '''

if "user_prompt" not in st.session_state:
    st.session_state.user_prompt = ""


# 4 sidebar

with st.sidebar:
    st.header("Pages")

    if st.button("Add New Defendant", use_container_width=True):
        st.session_state.btn1 = "Add New Defendant"
        st.session_state.btn2 = ""

    if st.button("Search by Name or ID", use_container_width=True):
        st.session_state.btn2 = "Search by Name or ID"
        st.session_state.btn1 = ""

if st.session_state.btn1 == "" and st.session_state.btn2 == "":
    st.info("Use the side bar on the top left to begin you application adventures.")

# 5 add new defendant

disabled = st.session_state.form_submitted

if st.session_state.btn1 == "Add New Defendant":
    with st_yled.container(
        background_color = GREEN,
        border_color = "#E4F6B3",
        padding = "20px"
    ):
        with st.form("Form"):
            st.title("Welcome to Hermany's AI Judge Template_24_Final")

            st.session_state.Name = st.text_input("Your Legal Name", disabled=disabled)

            st.session_state.ID = st.text_input("ID", disabled=disabled)

            st.subheader("Current Sentence Need to be Served", disabled=disabled)

            col1, col2 = st.columns(2)

            with col1:
                st.session_state.Penalties = st.radio(
                    "Penalties",
                    [
                        "Nothing(Cannot be Served)",
                        "Death Penalty",
                        "Death Reprieve",
                        "Life Imprisonment",
                        "Year Imprisonment"
                    ], 
                    disabled=disabled
                )

            with col2:
                st.session_state.Year = st.number_input(
                    "Year(if applicable)",
                    min_value = 0.0,
                    max_value = 10000.0,
                    step = 0.5,
                    value = 0.0, 
                    disabled=disabled
                )

            st.session_state.Case = st.text_area("Case Details If searching for a specific case type", disabled=disabled)

            st.session_state.Submit = st.form_submit_button("Submit", disabled=disabled)

    if st.session_state.Submit:

        
        if st.session_state.Name == "" or st.session_state.ID == "" or st.session_state.Case == "":
            st.session_state_Submit = True
            st.error("Please fill in all the required fields.")

        elif st.session_state.Penalties == "Year Imprisonment" and st.session_state.Year <= 0.0:
            st.error("If you choose Year Imprisonment, please enter a year bigger than 0.")

        elif st.session_state.Penalties != "Year Imprisonment" and st.session_state.Year > 0.0:
            st.error("If you did not choose Year Imprisonment, then please don't put any year")

        else:
            st.session_state.form_submitted = True
            st.rerun()
            st.success("Thanks for submission, Hermany will judge your case as soon as possible. Please wait patiently.")
            st.session_state.rule_prompt = '''
            a. You are fair
            b. You are impartial
            c. Even though you are helping the defendants, you cannot take pity or pleading. Or lean on the defendants to be purposely decreasing the sentence.
            d. Be FAIR
            e. BE IMPARTIAL
            f. NO PITY
            g. NO PLEADING
            h. If the defendants that was not wrongly convicted and have worse cases than should be punishes, like Cases> Punishments. You are able to add punishments to that denfendants.
            i. Give out the correct result.
                Like years, or what punishments
            '''

            st.session_state.Example = '''
            {
                "Result": "Write the result here",
                "Why do you have the result": "Write the reason here"
            }
            '''

            st.session_state.user_prompt = f'''
            You are a professional AI Judge. You will help those appeal defendants.

            Please strictly follow the rule:
            {st.session_state.rule_prompt}

            The defendant's name is {st.session_state.Name}.
            The defendant's ID is {st.session_state.ID}.
            The defendant's current sentence is {st.session_state.Year} years or {st.session_state.Penalties}.
            The case details are: {st.session_state.Case}.

            STRICTLY USE THIS JSON FORMAT:
            {st.session_state.Example}

            Return ONLY pure text JSON.
            Do not use markdown.
            Do not use ```json.
            Do not write anything outside the JSON.
            '''
            try:
                with st.spinner("PATIENT!, HERMANY'S JUDGING"):
                    st.session_state.response = client.chat.completions.create(
                        model = "gpt-4.1",
                        response_format = {"type": "json_object"},
                        messages = [
                            {
                                "role": "user",
                                "content": st.session_state.user_prompt
                            }
                        ],
                        timeout = 30
                    )
            
            


                pure_text_JSON = st.session_state.response.choices[0].message.content
            except Exception as e:
                st.error(f"Error generating response: {e}")
                pure_text_JSON = None
            # st.subheader("Pure Text JSON")
            # st.code(pure_text_JSON, language="json")

            try:
                st.session_state.Output = json.loads(pure_text_JSON)

                defendant_info = {
                    "Name": st.session_state.Name,
                    "ID": st.session_state.ID,
                    "Penalty": st.session_state.Penalties,
                    "Year": st.session_state.Year,
                    "Case": st.session_state.Case,
                    "Output": st.session_state.Output
                }

                st.session_state.dictionary[st.session_state.Name.lower()] = defendant_info
                st.session_state.dictionary[st.session_state.ID.lower()] = defendant_info

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Why do you have the result")
                    st.write(st.session_state.Output["Why do you have the result"])
                    

                with col2:
                    st.subheader("Result")
                    st.write(st.session_state.Output["Result"])
                    
            except:
                st.error("Error Occured During Generating")
                st.write("This is what the AI gave:")
                st.write(str(pure_text_JSON))
            if st.button("Add a New One"):
                st.session_state.form_submitted = False
                st.rerun()


# 6 search

if st.session_state.btn2 == "Search by Name or ID":

    st.title("Search by Name or ID")

    if len(st.session_state.dictionary) == 0:
        st.error("There is no wrongly convicted case in the database, please add new defendants to the database.")

    else:
        st.session_state.search_query = st.text_input("Search by Name or ID")

        if st.session_state.search_query:
            search_key = st.session_state.search_query.lower().strip()
            if search_key in st.session_state.dictionary:

                record = st.session_state.dictionary[search_key]
                output = record["Output"]

                st.success("Case found.")

                st.write("Name:", record["Name"])
                st.write("ID:", str(record["ID"]))
                st.write("Penalty:", record["Penalty"])
                st.write("Year:", str(record["Year"]))

                # st.subheader("Pure Text JSON")
                # st.code(json.dumps(output, indent=4), language="json")

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Why do you have the result")
                    st.write(output["Why do you have the result"])

                with col2:
                    st.subheader("Result")
                    st.write(output["Result"])

            else:
                st.error("No results found for the given Name or ID.")