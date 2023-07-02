import streamlit as st

# title of the app
st.title("Streamlit new chat elements")

# with st.chat_message("user"):
#     st.write("Hello 👋")

# with st.chat_message("assistant"):
#     st.write("Hello 👋 I'm assistant")


prompt = st.chat_input("Input here")
if prompt:
    st.markdown(f"Echo is working: {prompt}")