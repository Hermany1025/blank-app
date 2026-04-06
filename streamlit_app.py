import streamlit as st

st.title("Simple Streamlit Website")
st.header("User Input Section")
with st.form("Fprm"):


    s = st.text_input ("Your Name")
    e = st.text_area ("IDEA")
    w = st.selectbox("Type", ["Game", "Debate", "Wiki", "Email Generater", "Translate"])
    submit = st.form_submit_button("Submit") 
    succ = st.success("Generated")   
    if succ:
        st.write("Name", s, "\n", e, "\n", w)


st.slider("How far along are you", 0, 100)

pressed = st.button("Click me")
if pressed:
    st.write("You click me")
