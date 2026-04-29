import streamlit as st
import st_yled
import json
from openai import OpenAI
import random

st_yled.init()
client = OpenAI(api_key=st.secrets["OPENAIKEY"])
# GLOBAL CONTAINER
PRIMARY = "#E42121"
SECONDARY = "#3567FF"
TERTIARY= "#FFF700"
QUATERNARY= "#FF9500"
GRAY = "#535353"
GREEN = "#E4F6B3"
st_yled.set("button", "background_color", GREEN)
st_yled.set("write", "font_size", "20px")
# st_yled.set("write", "color", GREEN)
# ---------- SESSION STATE ----------
defaults = {
    "user": "",
    "start": False,
    "chat_history": [],
    "last_response": None
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ---------- UI ----------


# Create a container with a custom background and text color using markdown

# AI-assisted styling:
with st_yled.container():
    st.markdown(
        '''
        <style>
        .custom-container {
            background-color: #535353;
            padding: 10px;
            border-radius: 3px;
        }
        .custom-container p {
            color: #E42121;
            font-size: 24px;
            font-weight: bold;
        }
        .custom-container e {
            color: #3567FF;
            font-size: 20px;
            font-weight: bold;
        }
        .custom-container t {
            color: #FF9500;
            font-size: 10px;
            font-weight: bold;
        }
        </style>
        
        <!-- Dungeon Crawler Title -->
        <div class="custom-container">
            <p>HERMANY'S DUNGEON CRAWLER</p>
        </div>
        
        <!-- Template -->
        <div class="custom-container">
            <e>Template_23</e>
        </div>

        <!-- Copyright -->
        <div class="custom-container">
            <t>All Copywrite belonged to Hermany, Chinmany Seimens complany. "https://Chinmany_Seimens/Hermanys_Dungeon_Crawler_Game_template_23.cn.com"
        </div>
        ''',
        unsafe_allow_html=True
    )
    # st_yled.title("HERMANY'S DUNGEON CRAWLER", color=PRIMARY)
    # st_yled.subheader("Template_23", color = TERTIARY)
    # st_yled.write("All Copywrite belonged to Hermany, Chinmany Seimens complany. https://Chinmany_Seimens/Hermanys_Dungeon_Crawler_Game_template_23.cn.com", color = SECONDARY)

    
    col1, col2 = st.columns(2)
with col1:
    st_yled.badge_card_one(
        badge_text="Template_24",
        badge_icon=":material/square:",
        title="HEMANY'S DUNGEON CRAWLER",
        text="DUNGEON CRAWLER SETTING IN A MIDDLE SCHOOL"
    )
with col2:
    st_yled.badge_card_one(
        badge_text="Author's Note",
        badge_icon=":material/circle:",
        title="Author:",
        text="HERMAN HU"
    )

st.subheader("Game")
st.divider()

# ---------- FORM ----------
with st.form("form"):
    name_input = st.text_input("Enter your name")
    submitted = st_yled.form_submit_button("START", color = SECONDARY, background_color = GRAY)
# AI-assisted styling:
if submitted:
    if not name_input.strip():
        st.error("Please enter a name")
    else:
        st.session_state.user = name_input
        st.session_state.start = True

        # Initialize chat ONLY ONCE
        st.session_state.chat_history = [{
            "role": "system",
            "content": (
                "You are a dungeon game master.\n"
                "Return ONLY valid JSON.\n"
                "Format:\n"
                "{"
                "\"Description\": \"string\","
                "\"Choices\": [\"1. ...\", \"2. ...\", \"3. ...\"]"
                "}\n"
                "Setting: School. A dragon is trying to kidnap middle schoolers."
            )
        }]

# ---------- FUNCTION ----------
# AI-assisted styling:
def get_ai_response():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.chat_history
    )

    raw = response.choices[0].message.content

    try:
        parsed = json.loads(raw)
        st.session_state.last_response = parsed
        st.session_state.chat_history.append(
            {"role": "assistant", "content": raw}
        )
    except json.JSONDecodeError:
        st.error("AI returned invalid JSON. Try again.")
        st.write(raw)

# ---------- GAME START ----------
if st.session_state.start:

    st_yled.write(f"Welcome {st.session_state.user}")

    # First response
    if not st.session_state.last_response:
        st.session_state.chat_history.append(
            {"role": "user", "content": f"My name is {st.session_state.user}"}
        )
        get_ai_response()

    # Display response
    # ST_YLED WEBSITE-assisted styling:
    with st_yled.container(
    background_color="#f8f9fa",
    border_color="#dee2e6",
    padding="20px"
    ):
        # st_yled.text("Content inside styled container")
        if st.session_state.last_response:
            data = st.session_state.last_response
            
            st_yled.write(data.get("Description", ""))
    # ST_YLED WEBSITE-assisted styling:
    with st_yled.container(
    background_color="#f8f9fa",
    border_color="#dee2e6",
    padding="20px"
    ):
            choices = data.get("Choices", [])

            # Buttons
            cols = st.columns(3)
            for i, choice in enumerate(choices):
                with cols[i]:
                    if st_yled.button(choice):
                        st.session_state.chat_history.append({
                            "role": "user",
                            "content": f"I choose option {i+1}. Continue the game."
                        })
                        st.session_state.last_response = None
                        st.rerun()




# Application description
# 1. This Dungeon Crawler application was a game application with the association with OpenAI. This application is a game application mainly theme was Dungeon Crawler, the setting was a Middle School.
# 2. This application requires the user to first put in their name, then press TRATS or start. Then the OpenAI would provide the game information. Then based on the game description, choose one of the three choices provided to continue the game, after each round the description will refresh and generate a new description based on your choices.
# Reflection
# 1. There were many errors that I faced, for example, everytime that the user needs to enter there name to continue one round of a game everytime, but now use condition check, user can continue their game as many rounds as they want, until they leanve the game. Also the st_yled issues, style problems for me were background color with color in buttons write and many functions. Also I sometimes fail to visualise my theme color and theme in my game, those colors and visualizations were hard.
# 2. ST_YLED was super hard for me, especially those containers and global styling, it hard to add variables to containers, and the format of setting up container was first confusing, but slowly I get it. I mean styled is a good tool to visualize my Dungeon Crawler, but it is hard for me to combine colors with other colors, all does colors, font and border radius, was hard for me to visualize and convey theme in my Dungeon Crawler, I have litrally no inspirations, I can only use red, yellow, and orange, to convey theme, through fire, red, yellow, more fire, and orange, lava.
# 3. For ST_YLED I chose red, yellow, and orange for my main colors to visualize and convey my theme, these represent, fire, and lava. I can't think of any new colors. And also, I don't know anything about styling in styled, all I know is font size, color, background color, and padding, and border radius.
# BASICALLY MY WHOLE CODE WAS REVISED USING CHAT GPT BUT THE BASIC STRUCTURE WAS HERMAN MADE.