import streamlit as st

#create a conversational streamlit app using st.chat_message and st.chat_input
st.title("Streamlit Conversation App with ChatGPT like prompting delay")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type here")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    