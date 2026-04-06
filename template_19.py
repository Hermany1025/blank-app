# 1
import streamlit as st
from openai import OpenAI

# 2
client = OpenAI(
    api_key = st.secrets["OPENAIKEY"]
)

# 3
st.title("Hermany's Email Generater 'template_19'")
st.header("Developed in Germany Seimens Company")
st.write("All Copywrite belonged to Hermany, Chinmany Seimens complany. https://Chinmany_Seimens/Hermanys_Email_Generater_template_19.cn.com")
with st.form("Form"):
    user = st.text_input("User's(Your) name-> ")
    use = st.text_input("Recipient's name-> ")
    us = st.text_input("What kind of writing style you want-> ")
    u = st.text_area("What is the email about?-> ")
    se = st.text_input("Who is this email to in general-> ")
    submit = st.form_submit_button("Gen-er-ate") 
    if submit:
        if user == "" or use == "" or us == "" or u == "" or se == "":
            st.error("Missing info?")
        else:
            succ = st.success("Generated")
            user_prompt = f'''
            You will generate a Email, the person that sends the email is called string: "{user}", and the recipient's name is string: "{use}", please generate the email using the style of {us}, generate the email about {u}. NOTE: Please iclude user's name, Recipient's name, style of the email and what the emails about. IMPORTANT: PLEASE NEVER INCLUDE ANY WARNING AT THE END OF THE EMAIL AND NO EMOJIS. This email is generated to string: "{se}", so please make the email in the way that you talks to, string: "{se}"
            '''

            # 4
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )

            # 5
            st.write(response.choices[0].message.content)

#Application Description
# A. My Application will ask user about, User's Name, Reciptent's name, The style of writing of the email, and what is the email about, last it will ask what is this email to in general. This application generate a email with OpenAI.
# B. In this application there is one text_input(Asking User's Name), One text_input(The Recipient's name), a text_input(Asking the email and writing type) one text_area(A text area asking for what the email is about), and a text_input(Asking who is this email to in general), and lastly a submit_button(A button that submit the form and start generating the email using the information provided from the user by OpenAI).
# Reflection
# 1. Things that changed is to swap "input" to st.text_input, and st.text_area, and "print" to st.write, st.tittle and st.header, and a form created and a submit_button built.
# 2. It went pretty well, I didn't run into any errors and problems, and questions.
# 3. Input validation is important because without text validation, the OpenAI will keep running without any stop, it can eventually crash your code, and also the OpenAI will start running when the moment you open the website, but the user didn't put anything yet, and the user won't get a chance to input information.
# 4.If I didn't validate inputs then thee program will keep runing with wrong information, and eventually crash your code since it is always running without stopping, and also the user won't neven have a chance to input information, it is just gonna run blank informations to OpenAI, and generate nothing, first it waste tokens, second the user will have a bad experience and not able to input valide informartion to the form of the application.