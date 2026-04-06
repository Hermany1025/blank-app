import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key = st.secrets["OPENAIKEY"]
)
with st.form("Form"):
    st.title("Hermany's Template_18 Translator")
    user = st.selectbox("Select a language for INPUT-> ", ["English", "Chinese", "Korean", "Japanese"])
    use = st.text_area("INSERT YOUR MESSAGES-> ")
    us = st.selectbox("Select a language for OUTPUT-> ", ["English", "Chinese", "Korean", "Japanese"])
    submit = st.form_submit_button("Trans-late") 
    if submit:
        if use == "":
            st.error("Missing info?")
        else:
            succ = st.success("Generated")   
            user_prompt = f'''
            You are a translator. Please translate string: "{use}", From language  {user} to language {us} No, matter what, just translate, if it doesnt make sense, do your best. |PLEASE LABEL THE LANGUAGE TO THE ACCORDINGLY OUTPUT LANGUAGE| NOTE: ONLY GIVE THE TRANSLATION, PLEASE DO NOT DESCRIBE"
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

# My application "Hermany's Template_18 Translator" is based on Streamlit Python, it allows to translate from one word to a essay long translator, it allows to translate from English, Chinese, Korean, and Japanese to English, Chinese, Korean, and Japanese.
# The users' expected four input are first select you input language from a select box, there are four languages, English, Chinese, Korean, and Japanese. Then a input_area for your input message to translate from the origin language of your selected input language. Then another selectbox, that shows the output language or translated language message, you can select four languages, English, Chinese, Korean, and Japanese. Then last user's input is a "Submit" biutton, after pressing the "Submit" button, the message will start translating from the input language to the output language.
# Reflection
# 1. Things that changed from only prompt to application are changeing the prefix to "st." and any print are write and tittle, also instead of input language, it is select language from a selectbox, and adding "form" function to show a form, and instead of input, it is text area. Last the instead of pressing "Return" or "Enter" on the keyboard. It turns out to be a submit button, and it will start translating the messages that the user input.
# 2. Errors That occured during developing are form issues and submit button, because my scale is not stablized, so the form and submit buttons are my major errors during developing.
# 3. Input validarion are inportant because without them, the program can keep running and crash , because if there is nothing in the text box, the program will keep running without stopping and translating nothing, so input validation can check if the textbox is empty or not, if empty, then will show error, but if there is messages in the textbox, then the program will start translating and working.
# 4. If I did not validate inputs, then my program would start running without stop, and keep translating blank message in the text box, eventually it might crash. Also without validition inputs, users would have a bad experience.