# 1
import streamlit as st
import json
from openai import OpenAI

# 2
client = OpenAI(
    api_key = st.secrets["OPENAIKEY"]
)


# 3
st.title("This is Wiki of China")
st.subheader("This is a Wiki that has varies of informations about CHINA!")
st.write("All Copywrite belonged to Hermany, Chinmany Seimens complany. https://Chinmany_Seimens/Hermanys_Wiki_China_template_20.cn.com")
st.divider()
user_prompt = '''
Warning: The first letter of the key needs to be captilized.
Please generate a five page wikipedia about China. Each topic is going to be one page, using json file and json format
Topic 1(Page 1): Generate a one page article about The Great Wall of China. How it made, purpose,and when it is built. Also the cost of crafting the Great Wall nof China.
Topic 2(Page 2): Generate a one page article about Modern Chinese History, include major events, like wars, accomplishments, and celebrities. And Ancient Chinese History, include all the dynasties, inventions, accomplishments, wars, major events, and celebrities.
Topic 3(Page 3): Generate a one page article about The World War II mainly focused on China. What significent and major events happend for China. When does the War start? When does it end? And some wars around this time period.
Topic 4(Page 4): Generate a one page article about Chinese Military, like weapons, aircrafts, seacrafts, and navy, army, and airforce. Major accomplishments, like inventions. And talking about military accomplishments. Some military wars around the time.
Topic 5(Page 5): Generate a one page article about Chinese Economy, like stocks, currencies. Also histry about Chinese Yuan. Events happened to Chinese Economy, modern trading with nearby countries.
Topic 6(Page 6): Generate a page of article of China of Chinese Cuisine.


For Example:
{
    "The_Great_Wall_of_China":
    {
        "Inoformation": str,
        "Conclusion": str,
    },
    "Modern_Chinese_History_and_Ancient_Chinese_History":
    {
        "Inoformation": str,
        "Conclusion": str,
    },
    "The_World_War_II":
    {
        "Inoformation": str,
        "Conclusion": str,
    },
    "Chinese_Military":
    {
        "Inoformation": str,
        "Conclusion": str,
    },
    "Chinese_Economy":
    {
        "Inoformation": str,
        "Conclusion": str,
    },
    "Chinese_Cuisine":
    {
        "Inoformation": str,
        "Conclusion": str,
    }
}

In the format that json can decode. Do not do whatever formatting you found incorrect

IMPORTANT: Don't print (```json - ```) 
'''
if "ss" not in st.session_state:
    st.session_state.ss = False
if "sss" not in st.session_state:
    st.session_state.sss = ()
if st.session_state.ss == False:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )
    # st.write("\n\n",response.choices[0].message.content)
    st.session_state.sss = json.loads(response.choices[0].message.content)
    # st.write(st.session_state.sss)
    st.session_state.ss = True


ts = st.selectbox("New Pages?", ["Nothing Here", "Yes", "No"])


with st.sidebar:
    st.header("Pages")
    btn1 = st.button("The Great Wall", use_container_width=True)
    btn2 = st.button("Modern Chinese History and Ancient Chinese History", use_container_width=True)
    btn3 = st.button("The World War II", use_container_width=True)
    btn4 = st.button("Chinese Military", use_container_width=True)
    btn5 = st.button("Chinese Economy", use_container_width=True)
    if ts == "Yes":
        btn6 = st.button("Extension Page (Chinese Cuisine)", use_container_width=True)
if ts == "Nothing Here":
    if not (btn1 or btn2 or btn3 or btn4 or btn5):
        st.info("Use the side bar to navigate to the page you want")
if ts == "No":
    st.write("Thank You for your response")
    st.divider()
    if not (btn1 or btn2 or btn3 or btn4 or btn5):
        st.info("Use the side bar to navigate to the page you want")
if ts == "Yes":
    if not (btn1 or btn2 or btn3 or btn4 or btn5 or btn6):
        st.info("Use the side bar to navigate to the page you want")



if btn1:
    st.subheader("The Great Wall of China")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Information")
        st.write(st.session_state.sss["The_Great_Wall_of_China"]["Information"])
    with col2:
        st.subheader("Conclusion")
        st.write(st.session_state.sss["The_Great_Wall_of_China"]["Conclusion"])
elif btn2:
    st.subheader("Modern Chinese History and Ancient Chinese History")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Information")
        st.write(st.session_state.sss["Modern_Chinese_History_and_Ancient_Chinese_History"]["Information"])
    with col2:  
        st.subheader("Conclusion")  
        st.write(st.session_state.sss["Modern_Chinese_History_and_Ancient_Chinese_History"]["Conclusion"])
elif btn3:
    st.subheader("The World War II")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Information")
        st.write(st.session_state.sss["The_World_War_II"]["Information"])
    with col2:
        st.subheader("Conclusion")
        st.write(st.session_state.sss["The_World_War_II"]["Conclusion"])
elif btn4:
    st.subheader("Chinese Military")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Information")
        st.write(st.session_state.sss["Chinese_Military"]["Information"])
    with col2:
        st.subheader("Conclusion")
        st.write(st.session_state.sss["Chinese_Military"]["Conclusion"])
elif btn5:
    st.subheader("Chinese Economy")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Information")
        st.write(st.session_state.sss["Chinese_Economy"]["Information"])
    with col2:
        st.subheader("Conclusion")
        st.write(st.session_state.sss["Chinese_Economy"]["Conclusion"])
#Extension
if ts == "Yes":
    if btn6:
        st.subheader("Extension page (Chinese Cuisine)")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Information")
            st.write(st.session_state.sss["Chinese_Cuisine"]["Information"])
        with col2:
            st.subheader("Conclusion")
            st.write(st.session_state.sss["Chinese_Cuisine"]["Conclusion"])
        
# Application
# Expected users to navighate through pages, through the navigation sidebar
# This Wiki of China was a Wikipedia copied version of Wiki. There are five pages, The Great Wall of China, Modern Chinese History and Ancient Chinese History, The World War II, Chinese Military, Chinese Economy, Extension page Chinese Cuisine
# 1. Things that changed from terminal based program to a Streamlit app were adding a divider(st.divider()) and changing print into st.tittle, st.header, st.subheader and st.write, also there were navigation bar for going to six different pages of the Wiki.
# 2. Errors that occured during my programming are two, one of them is the st.subheader() order problem because I put the column code on top of the page if statement code, so all my subheader was at the bottom of my page, but after I put column code in every if statementunder the st.subheader, it turns out normal. Last it was the stat.session, because without state session, every time I did a action like navigate to a page, ChatGPT always reloads, so everytime I did an action the program's ChatGPT reruns and reloads all the time, but now I put ChatGPT in a state sassion, it won't reload all the time, so my navigate, turns out normal, with Chat GPT printed out.
# 3. It is important to validate Chat GPT generate response before users navigate because, if users navigate before Chat GPT, the pages would be all blank, and the page will start loading Chat GPT generating information very slow,and if users validate before, the accessing code is on top of the Chat GPT response, can cause the accessing code can't access any information, since the accessing code is on top of the Chat GPT responses, so Chat GPT can't be accessed.
# 4. If you call the API every time the user selected a page instead of storing the results then the information was not saved, since everytime the API reloads and regenerate the information. Also your program will be very slow, because everytime you naviagte to a page, it reloads and regenerate the API all the time, so you program can be very slow. Also If you want to go back to the previous page all your information will be losted. But with a one time call API, the information will only be generated once, and so everytime you access a page will be very fast, and the information will only be loaded once and for the next time you navigate to a page, it won't reload and even though you exit out a page when you go back to the previous page, your informations were safed and able to be seen again.