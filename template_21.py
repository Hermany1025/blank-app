# 1
import streamlit as st
import json
from openai import OpenAI

# 2

st.title("Hermany's Pokemon Gernater")
st.subheader("Template_21")
st.write("All Copywrite belonged to Hermany, Chinmany Seimens complany. https://Chinmany_Seimens/Hermanys_Pokemon_Pokedex_Gernater_template_21.cn.com")
st.divider()
client = OpenAI(
    api_key = st.secrets["OPENAIKEY"]
)

dictionary = {}
prompt = '''
{
    "Name": str,
    "Four Digit ID": int,
    "Stats":
    {
        "An HP Value": int,
        "An Attack Value": int,
        "A defense value": int,
        "A speed value": int
    },
    "Description": str
    "Details":
    {
        "Gender": str,
        "Category(Type of creature)": str,
        "A list of abilities": str
    },
    "It's Type":
    {
        "It's type(water/earth etc…, a pokemon can have 1 or 2 types)": str
    },
    "Pokemon's weak points":
    {
        "A list of weak points that this Pokemon have": str
    },
    "Evolves":
    {
        "What the Pokemon Evolves to": str
    }
}
'''

# Create sesssion state variables if they do not exist 
if "mit" not in st.session_state:
     st.session_state.mit = False
if "sub" not in st.session_state:
     st.session_state.sub = False
if "form_active" not in st.session_state:
    st.session_state.form_active = False
if "di" not in st.session_state:
     st.session_state.di = {}

if st.button("Show Pokemon"):
    st.session_state.form_active = False
    st.session_state.sub = True
if st.button("Add Pokemon"):
    st.session_state.form_active = True
    st.session_state.sub = False

if st.session_state.form_active:
    # 3
    with st.form("Form"):
        user = st.text_input("Pokedex Name-> ")
        submit = st.form_submit_button("Gen-er-ate")
        if submit:
            if user == "":
                st.error("Missing info")
            else:
                user_prompt = f'''
                ***IMPORTANT: *** GENERATE IN THE WAY THAT THE JSON FILE CAN DECODE IM BEGGING YOU PLEASE******
                This is a Pokemon generater, you are the generater. Generate a Pokemon caled string: {user} then generate {prompt}. PLEASE FOLLOW THE JOSON FORMAT THAT JSON CAN DECODE. DO NOT INCLUDE (```json - ```).
                WARNING: DO NOT INCLUDE (```json - ```)
                '''
                

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "user", "content": user_prompt + "***Priority Rule: IMPORTANT: DO NOT INCLUDE (```json - ```)***"}
                    ]
                )

                print("\n\n",response.choices[0].message.content)
                di = json.loads(response.choices[0].message.content)
                # st.write(di)
                st.session_state.di[user] = di
                dictionary = di
                # Ask chatgpt with user prompt here
                # decode with json.loads
                # add 'di' to 'dictionary' 
                # for key in dictionary:
                #     # st.write(key, dictionary[key])
                st.subheader("Pokemon:", dictionary["Name"])
                col1, col2 = st.columns(2)
                with col1:
                    st.write("Name:", dictionary["Name"])
                    st.write("Four digit ID:", str(dictionary["Four Digit ID"]))
                    st.write("Stats: HP Value:", str(dictionary["Stats"]["An HP Value"]))
                    st.write("Stats: Attack Value:", str(dictionary["Stats"]["An Attack Value"]))
                    st.write("Stats: Defense Value:", str(dictionary["Stats"]["A defense value"]))
                    st.write("Stats: Speed Value:", str(dictionary["Stats"]["A speed value"]))
                with col2:
                    st.write("Details: Gender:", dictionary["Details"]["Gender"])
                    st.write("Details: Category:", dictionary["Details"]["Category(Type of creature)"])
                    st.write("Details: Abilities:", dictionary["Details"]["A list of abilities"])
                    st.write("It's Type:", dictionary["It's Type"]["It's type(water/earth etc…, a pokemon can have 1 or 2 types)"])
                    st.write(user + "'s weak points:", dictionary["Pokemon's weak points"]["A list of weak points that this Pokemon have"])
                    st.write("Evolves:", dictionary["Evolves"]["What the Pokemon Evolves to"])

if st.session_state.sub:
    if len(st.session_state.di) == 0:
            st.error("There is no Pokemons! TRY AGAIN!")
    else:
        st.success("Here you Go")
        num = 0
        for key in st.session_state.di:
            num = num + 1
            st.subheader("Pokemon" + str(num)+ ":", st.session_state.di[key]["Name"])
            col1, col2 = st.columns(2)
            with col1:
                st.write("Name:", st.session_state.di[key]["Name"])
                st.write("Four digit ID:", str(st.session_state.di[key]["Four Digit ID"]))
                st.write("Stats: HP Value:", str(st.session_state.di[key]["Stats"]["An HP Value"]))
                st.write("Stats: Attack Value:", str(st.session_state.di[key]["Stats"]["An Attack Value"]))
                st.write("Stats: Defense Value:", str(st.session_state.di[key]["Stats"]["A defense value"]))
                st.write("Stats: Speed Value:", str(st.session_state.di[key]["Stats"]["A speed value"]))
            with col2:
                st.write("Details: Gender:", st.session_state.di[key]["Details"]["Gender"])
                st.write("Details: Category:", st.session_state.di[key]["Details"]["Category(Type of creature)"])
                st.write("Details: Abilities:", st.session_state.di[key]["Details"]["A list of abilities"])
                st.write("It's Type:", st.session_state.di[key]["It's Type"]["It's type(water/earth etc…, a pokemon can have 1 or 2 types)"])
                st.write(st.session_state.di[key]["Name"], "'s weak points:", st.session_state.di[key]["Pokemon's weak points"]["A list of weak points that this Pokemon have"])
                st.write("Evolves:", st.session_state.di[key]["Evolves"]["What the Pokemon Evolves to"])
#Application Description
#This app application, was created base on the python file and Json file, with app application. This application uses ChatGPT to generate A Pokemon Pokedex
#This app requires the user to push one out of the two buttons to start, then a text input of Pokemon names is rquired, finally a submit button, lastly the new round of a button is rquired.
#Reflection
#1. Things that changed drom Python terminal to Streamlit Application were print to st.write, st.tittle, and st. subheader, input to St.text_input, and adding at.button, st.form_submit_button instead of doing return key on the keyboard.
#2. Errors that occurred during developing were ChatGPT jaon file error with ('''-'''json) and json not able to be accessed because in a for loop, also the key was not being able to be defined, lastly was the session state not being used. causing the information not being formed, which caused the buttons not working.
#3. 'st.session_state' was a deature that prevent you information being reset everytime the orogram reruns, this prevent information being reset, which if you want to show information after an action. the information us still being saved. The st.session_state is important in this application because this function can save the information of the Pokemon Pokedex, so when viewing all the Pokemons, the information will be safed and will not be reseted when the program reruns or got reset.
#4. If 'st.session_state' was not used, then your information of a pokemon pokedex can be reset, and unable to access the inormation, after adding a pokemon the view the pokemon, but if you use session state, then your informations will be saved instead of being reset everytime the program reruns.
# IN THE ORIGINAL PROJECT, THERE IS NO EXTENSION PARTS