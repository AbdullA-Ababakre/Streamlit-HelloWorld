import streamlit as st
import random
import time

#create a conversational streamlit app using st.chat_message and st.chat_input
st.title("Streamlit Conversation App with ChatGPT like prompting delay")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type here")

if prompt:

    st.session_state.messages.append({"role":"user","content":prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = random.choice([
            "I am a chatbot. I am here to help you.",
            "What can I do for you?",
            "Do you have any questions for me?"
        ])
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "...")
        message_placeholder.markdown(full_response)

    # add asststant response to chat history
    st.session_state.messages.append({"role":"assistant","content":full_response})