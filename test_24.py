import streamlit as st
import st_yled

st.set_page_config(page_title="Badge and Button Demo", page_icon="✨", layout="centered")

# Initialize st_yled
st_yled.init()

st.title("Styled Badge and Button Demo")

# Built-in Streamlit badge
st.badge("New Feature", icon=":material/star:", color="violet")

st.write("Click the styled button below:")

# Styled button using st_yled
clicked = st_yled.button(
    "Launch",
    type="primary",
    background_color="#6C63FF",
    color="white",
    border_color="#4B44CC",
    border_style="solid",
    border_width=2,
)
hh = st_yled.button(
    "Launch",
    type="primary",
    background_color="#6C63FF",
    color="white",
    border_color="#E42121",
    border_style="solid",
    border_width=2,
)

if clicked:
    st.success("Button clicked!")