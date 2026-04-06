import streamlit as st
from openai import OpenAI
import time

# ============================================================
# Define all variables here
# ============================================================
client = OpenAI(
    api_key = st.secrets["OPENAIKEY"]
)

with st.form ("Form"):
    debater_A = st.text_input("Choose a debater of a character: ", key = "1")
    debater_B = st.text_input("Choose a debater of a character: ", key = "2")
    trait_1 = st.text_input(debater_A + "'s trait", key = "3")
    trait_2 = st.text_input(debater_B + "'s trait", key = "4")
    style1 = st.text_input(debater_A + "'s trait", key = "5")
    style2 = st.text_input(debater_B + "'s trait", key = "6")
    topic = st.text_input("Coose a topic: ", key = "7")
    submit = st.form_submit_button("TIMBUS")
if submit:
    if (debater_A or debater_B or trait_1 or trait_2 or style1 or style2 or topic) == "":
        st.error("Missing Info?")
    else:
        A_prompt = f'''
        You are {debater_A}, a democracy debater.
        You are arguing {debater_B} the topic: {topic}.
        Your debate style is ***casual***.
        Follow these rules:
        - Present logical arguments with supporting evidence
        - Directly address points made by your opponent
        - Stay on topic and maintain your position
        - Use ***casual*** tone in your responses
        - Keep responses between 3-5 sentences
        - Do not concede your position, but acknowledge valid counterpoints
        Each response should include:
        - A main argument or counterargument
        - Supporting reasoning or evidence
        - A question or challenge to your opponent
        '''
        B_prompt = f'''
        You are {debater_B}, a communism debater.
        You are arguing {debater_A} the topic: {topic}.
        Your debate style is ***formal***.
        Follow these rules:
        - Present logical arguments with supporting evidence
        - Directly address points made by your opponent
        - Stay on topic and maintain your position
        - Use ***formal*** tone in your responses
        - Keep responses between 3-5 sentences
        - Do not concede your position, but acknowledge valid counterpoints
        Each response should include:
        - A main argument or counterargument
        - Supporting reasoning or evidence
        - A question or challenge to your opponent
        '''



        # Store debate rounds
        debate_rounds = []

        # ============================================================
        # Create opening statements / start debate history / add to history
        # ============================================================
        # Create person A chat history
        chat_history_A = [
            {"role": "system", "content": A_prompt},
            {"role": "user", "content": f"Give your opening statement on: {topic}"}
        ]
        # Generate person A opening statements
        response_A = client.chat.completions.create(
            model="gpt-4o",
            messages=chat_history_A
        )
        # Adding what person A said to their history
        message_A = response_A.choices[0].message.content
        chat_history_A.append({"role": "assistant", "content": message_A})

        # Create person B chat history
        chat_history_B = [
            {"role": "system", "content": B_prompt},
            {"role": "user", "content": f"The topic is: {topic}. Your opponent says: {message_A}. Respond with your opening statement."}
        ]
        # Generate person B opening statements
        response_B = client.chat.completions.create(
            model="gpt-4o",
            messages=chat_history_B
        )
        # Adding what person B said to their history
        message_B = response_B.choices[0].message.content
        chat_history_B.append({"role": "assistant", "content": message_B})

        # Conduct 3 rounds of rebuttals hp
        # NOTE - You need to add what the other character said within the user_prompt so the characters know what their opponent replied with
        st.write(f"\n{'='*60}")
        st.write(f"Opening Statement")
        st.write(f"{'='*60}\n")
        chat_history_A.append({"role": "user", "content": "{debater_A} said this for their opening statement: {response_A.choices[0].message.content} \n Please provide your opening statement of your debate with Mao Zedong. Like how you greet a person when you guys first met."})
        response_A = client.chat.completions.create(
            model="gpt-4o",
            messages=chat_history_A
        )
            
        chat_history_A.append({"role": "assistant", "content": response_A.choices[0].message.content})
        st.write(debater_A)
        st.write(response_A.choices[0].message.content)
        

        chat_history_B.append({"role": "user", "content": "{debater_B} said this for their opening statement: {response_B.choices[0].message.content} \n Please provide your opening statement of your debate with Mac Arthur. Like how you greet a person when you guys first met."})
        response_B = client.chat.completions.create(
            model="gpt-4o",
            messages=chat_history_B
        )
            
        chat_history_B.append({"role": "assistant", "content": response_B.choices[0].message.content})
        st.write(debater_B)
        st.write(response_B.choices[0].message.content)
        for round_num in range(1, 4):
            st.write(f"\n{'='*60}")
            st.write(f"ROUND {round_num}")
            st.write(f"{'='*60}\n")
            
            # YOUR CODE HERE: 
            # 1. Generate Debater A's rebuttal w/ Debater B's opening statement included in prompt
            chat_history_A.append({"role": "user", "content": "{debater_A} said this for their statement: {response_A.choices[0].message.content} \n Please provide your rebuttal for this statement"})
            response_A = client.chat.completions.create(
                model="gpt-4o",
                messages=chat_history_A
            )
            # 2. Add to Debater A's history
            chat_history_A.append({"role": "assistant", "content": response_A.choices[0].message.content})
            st.write(debater_A)
            st.write(response_A.choices[0].message.content)
            # 3. Generate Debater B's response w/ Debater A's rebuttal included in propmt
            chat_history_B.append({"role": "user", "content": "{debater_B} said this for their statement: {response_B.choices[0].message.content} \n Please provide your rebuttal for this statement"})
            response_B = client.chat.completions.create(
                model="gpt-4o",
                messages=chat_history_B
            )
            # 4. Add to Debater B's history
            chat_history_B.append({"role": "assistant", "content": response_B.choices[0].message.content})
            st.write(debater_B)
            st.write(response_B.choices[0].message.content)
            time.sleep(1)
            
        # YOUR CODE HERE: Generate closing statements for both debaters
            
        st.write(f"\n{'='*60}")
        st.write(f"Closing Statement")
        st.write(f"{'='*60}\n")
        chat_history_A.append({"role": "user", "content": "{debater_A} said this for their ending statement: {response_A.choices[0].message.content} \n Please provide your ending statement of your debate with Mao Zedong. Like how you say good bye to a person when you guys are about to leave."})
        response_A = client.chat.completions.create(
            model="gpt-4o",
            messages=chat_history_A
        )
            
        chat_history_A.append({"role": "assistant", "content": response_A.choices[0].message.content})
        st.write(debater_A)
        st.write(response_A.choices[0].message.content)

        chat_history_B.append({"role": "user", "content": "{debater_B} said this for their ending statement: {response_B.choices[0].message.content} \n Please provide your ending statement of your debate with Mac Arthur. Like how you say good bye to a person when you guys are about to leave."})
        response_B = client.chat.completions.create(
            model="gpt-4o",
            messages=chat_history_B
        )
            
        chat_history_B.append({"role": "assistant", "content": response_B.choices[0].message.content})
        st.write(debater_B)
        st.write(response_B.choices[0].message.content)

        # Finished

        # Mac Arhur(Casusal Debater) and Mao Zedong (Formal Debater) was debating about which country is better in the years of 1950s.