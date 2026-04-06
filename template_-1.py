import streamlit as st


sa = ("")
st.title("Creature Creator")
st.header("Design your creature")
with st.form("Form"):
    col1, col2 = st.columns(2)
    with col1:
        s = st.text_input ("Creature Name")
        e = st.text_area ("CREATURE ORIGIN")
    with col2:
        w = st.selectbox("Creature Type", ["Dragon", "Spirit", "Robot", "Alien", "Unknown"])
        we = st.radio("Personality: ", ["Aggressive", "Calm", "Mysterious", "Chaotic"])
    Spam = st.number_input("Lifespan (years)", min_value=0, max_value=10000, value=500) 
    spa = st.multiselect("Special Abilities", ["Fire Control", "Mind Reading", "Teleportation", "Invisibility", "Super Strength"])
    sd = st.text_area("Write a short backstory")
    ag = st.checkbox("Include a weakness")
    if ag:
        sa = st.text_input("Weakness: ")
    submit = st.form_submit_button("Generate") 
    if "submit" not in st.session_state:
        st.session_state.submit = False   
if submit:
    if sd == "" or s == "" or e == "" or w == "" or we == "" or Spam == "" or spa == "":
        st.error("Missing info?")
    else:
        if sa == "":
            st.success("Generated")
            st.success("Generated")
            st.write("Name: ", s)
            st.write("Origin: ", e)
            st.write("Creature type: ", w)
            st.write("Personality: ", we)
            st.write("Lifespan(years): ", Spam)
            st.write("Special Abilitie: ", spa)
            st.write("Short Backstory: ", sd)
            st.write("Weakness: None")
        else:
            st.success("Generated")
            st.write("Name: ", s)
            st.write("Origin: ", e)
            st.write("Creature type: ", w)
            st.write("Personality: ", we)
            st.write("Lifespan(years): ", Spam)
            st.write("Special Abilitie: ", spa)
            st.write("Short Backstory: ", sd)
            st.write("Weakness: ", sa)




