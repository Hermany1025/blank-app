import streamlit as st
import json
from openai import OpenAI

# ---------------- TITLE / CREATIVE THEME ----------------

st.title("Hermany's Pokemon Gernater")
st.subheader("Template_24_Final")
st.write("All Copywrite belonged to Hermany, Chinmany Seimens complany. https://Chinmany_Seimens/Hermanys_AI_Judge_template_24_Final.cn.com")
st.divider()

client = OpenAI(
    api_key=st.secrets["OPENAIKEY"]
)

# ---------------- SESSION STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = ""

if "Output" not in st.session_state:
    st.session_state.Output = {}

if "dictionary" not in st.session_state:
    st.session_state.dictionary = {}

if "response" not in st.session_state:
    st.session_state.response = ""

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.header("Pages")

    if st.button("Add New Defendant", use_container_width=True):
        st.session_state.page = "Add New Defendant"

    if st.button("Search by Name or ID", use_container_width=True):
        st.session_state.page = "Search by Name or ID"

# ---------------- ADD NEW DEFENDANT PAGE ----------------

if st.session_state.page == "Add New Defendant":

    with st.form("Form"):
        st.title("Welcome to Hermany's AI Judge Template_24_Final")

        Name = st.text_input("Your Legal Name")
        ID = st.text_input("ID")

        st.subheader("Current Sentence Need to be Served")

        col1, col2 = st.columns(2)

        with col1:
            Penalties = st.radio(
                "Penalties",
                [
                    "Nothing(Cannot be Served)",
                    "Death Penalty",
                    "Death Reprieve",
                    "Life Imprisonment",
                    "Year Imprisonment"
                ]
            )

        with col2:
            Year = st.number_input(
                "Year",
                min_value=0.0,
                max_value=10000.0,
                step=0.5,
                value=0.0
            )

        Case = st.text_area("Case Details If searching for a specific case type")

        Submit = st.form_submit_button("Submit")

    if Submit:
        st.write("Hermany is judging your case, please wait patiently.")

        if Name == "" or ID == "" or Case == "":
            st.error("Please fill in all the required fields.")

        elif Penalties == "Year Imprisonment" and Year <= 0.0:
            st.error("If the penalty is Year Imprisonment, please enter a year greater than 0.")

        else:
            st.success("Thanks for submission, Hermany will judge your case as soon as possible. Please wait patiently.")

            rule_prompt = """
            a. You are fair
            b. You are impartial
            c. Even though you are helping the defendants, you cannot take pity or pleading.
            d. Be FAIR
            e. BE IMPARTIAL
            f. NO PITY
            g. NO PLEADING
            """

            user_prompt = f"""
            You are a professional AI Judge. You will help those appeal defendants.

            Please strictly follow these rules:
            {rule_prompt}

            Defendant information:
            Name: {Name}
            ID: {ID}
            Current sentence years: {Year}
            Penalty: {Penalties}
            Case details: {Case}

            Return ONLY valid JSON.
            Do not use markdown.
            Do not add extra explanation outside the JSON.

            Use exactly this JSON format:
            {{
                "Result": "Write the result here",
                "Why do you have the result": "Write the reason here"
            }}
            """

            response = client.chat.completions.create(
                model="gpt-4o",
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "system",
                        "content": "Return only valid JSON. No markdown. No extra text."
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )

            pure_text_json = response.choices[0].message.content.strip()

            try:
                parsed_output = json.loads(pure_text_json)

                defendant_record = {
                    "Name": Name,
                    "ID": ID,
                    "Penalty": Penalties,
                    "Year": Year,
                    "Case": Case,
                    "Output": parsed_output
                }

                # Save into dictionary by Name and by ID
                st.session_state.dictionary[Name.lower()] = defendant_record
                st.session_state.dictionary[ID.lower()] = defendant_record

                # Keep Output updated too
                st.session_state.Output = st.session_state.dictionary

                st.subheader("Pure Text JSON")
                st.code(
                    json.dumps(parsed_output, indent=4, ensure_ascii=False),
                    language="json"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Why do you have the result")
                    st.write(parsed_output["Why do you have the result"])

                with col2:
                    st.subheader("Result")
                    st.write(parsed_output["Result"])

            except json.JSONDecodeError:
                st.error("The response was not valid JSON.")
                st.subheader("Raw Output")
                st.code(pure_text_json)

# ---------------- SEARCH PAGE ----------------

elif st.session_state.page == "Search by Name or ID":

    st.title("Search by Name or ID")

    if len(st.session_state.dictionary) == 0:
        st.error("There is no wrongly convicted case in the database, please add new defendants to the database.")

    else:
        search_query = st.text_input("Search by Name or ID")

        if search_query:
            search_key = search_query.lower().strip()

            if search_key in st.session_state.dictionary:
                record = st.session_state.dictionary[search_key]
                output = record["Output"]

                st.success("Case found.")

                st.write("Name:", record["Name"])
                st.write("ID:", record["ID"])
                st.write("Penalty:", record["Penalty"])
                st.write("Year:", record["Year"])

                st.subheader("Pure Text JSON")
                st.code(
                    json.dumps(output, indent=4, ensure_ascii=False),
                    language="json"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Why do you have the result")
                    st.write(output["Why do you have the result"])

                with col2:
                    st.subheader("Result")
                    st.write(output["Result"])

            else:
                st.error("No results found for the given Name or ID.")

# ---------------- DEFAULT PAGE ----------------

else:
    st.info("Please choose a page from the sidebar.")