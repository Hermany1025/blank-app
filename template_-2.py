import streamlit as st

wiki_data = {
    "Zeus": {
        "name": "Zeus",
        "history": "Zeus is the king of the Olympian gods and ruler of Mount Olympus. He overthrew his father Cronus and divided the world among his brothers.",
        "characteristics": "God of the sky and thunder. Known for wielding a lightning bolt. Often depicted as a powerful bearded man.",
        "trivia": ["His Roman equivalent is Jupiter.", "He had over 100 children.", "His symbol is the eagle."]
    },
    "Athena": {
        "name": "Athena",
        "history": "Athena is the goddess of wisdom and war strategy. She was born fully armored from the forehead of Zeus.",
        "characteristics": "Known for intelligence over brute strength. Patron goddess of Athens. Often shown with an owl and olive branch.",
        "trivia": ["Her Roman equivalent is Minerva.", "She never had a romantic partner.", "She gifted the olive tree to Athens."]
    },
    "The Underworld": {
        "name": "The Underworld",
        "history": "The Underworld is the realm of the dead ruled by Hades. Souls travel there after death guided by Hermes.",
        "characteristics": "Divided into regions like Elysium and Tartarus. Surrounded by rivers including the Styx and Lethe.",
        "trivia": ["The three-headed dog Cerberus guards the entrance.", "Only a few heroes ever escaped alive.", "Charon ferries souls across the Styx."]
    },
    "The Olympians": {
        "name": "The Olympians",
        "history": "The Twelve Olympians are the major gods who reside on Mount Olympus. They rose to power after defeating the Titans.",
        "characteristics": "Each controls a domain of life. They interact with mortals frequently and often quarrel among themselves.",
        "trivia": ["There are actually 14 gods sometimes listed.", "They drink nectar and eat ambrosia.", "Mount Olympus is the highest peak in Greece."]
    },
    "The Trojan War": {
        "name": "The Trojan War",
        "history": "The Trojan War was a legendary conflict between Greece and Troy. It began after Paris of Troy took Helen from her husband Menelaus.",
        "characteristics": "Lasted ten years. Involved gods taking sides. Ended with the famous Trojan Horse trick.",
        "trivia": ["Homer's Iliad covers part of the war.", "Troy is believed to be in modern-day Turkey.", "Achilles was the greatest Greek warrior."]
    }
}

st.title("📖 Ancient Greek Mythology Wiki")
st.divider()

with st.sidebar:
    st.header("Pages")
    btn1 = st.button("Zeus", use_container_width=True)
    btn2 = st.button("Athna", use_container_width=True)
    btn3 = st.button("The Underworld", use_container_width=True)
    btn4 = st.button("The Olympians", use_container_width=True)
    btn5 = st.button("The Trojan War", use_container_width=True)
if not (btn1 or btn2 or btn3 or btn4 or btn5):
    st.info("Use the side bar to navigate to the page you want")

if btn1:
    st.subheader("Zeus")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("History")
        st.write(wiki_data["Zeus"]["history"])
        st.subheader("Characteristics")
        st.write(wiki_data["Zeus"]["characteristics"])
    with col2:
        st.subheader("Trivia")
        for i in range(len(wiki_data["Zeus"]["trivia"])):
            st.write(str(i+1)+".",wiki_data["Zeus"]["trivia"][i])
        
if btn2:
    st.subheader("Athena")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("History")
        st.write(wiki_data["Athena"]["history"])
        st.subheader("Characteristics")
        st.write(wiki_data["Athena"]["characteristics"])
    with col2:
        st.subheader("Trivia")
        for i in range(len(wiki_data["Athena"]["trivia"])):
            st.write(str(i+1)+".",wiki_data["Athena"]["trivia"][i])
if btn3:
    st.subheader("The Underworld")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("History")
        st.write(wiki_data["The Underworld"]["history"])
        st.subheader("Characteristics")
        st.write(wiki_data["The Underworld"]["characteristics"])
    with col2:
        st.subheader("Trivia")
        for i in range(len(wiki_data["The Underworld"]["trivia"])):
            st.write(str(i+1)+".",wiki_data["The Underworld"]["trivia"][i])
if btn4:
    st.subheader("The Olympians")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("History")
        st.write(wiki_data["The Olympians"]["history"])
        st.subheader("Characteristics")
        st.write(wiki_data["The Olympians"]["characteristics"])
    with col2:
        st.subheader("Trivia")
        for i in range(len(wiki_data["The Olympians"]["trivia"])):
            st.write(str(i+1)+".",wiki_data["The Olympians"]["trivia"][i])
if btn5:
    st.subheader("The Trojan War")
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("History")
        st.write(wiki_data["The Trojan War"]["history"])
        st.subheader("Characteristics")
        st.write(wiki_data["The Trojan War"]["characteristics"])
    with col2:
        st.subheader("Trivia")
        for i in range(len(wiki_data["The Trojan War"]["trivia"])):
            st.write(str(i+1)+".",wiki_data["The Trojan War"]["trivia"][i])