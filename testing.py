import streamlit as st
import base64 
from pypdf import PdfReader
# title of the app
st.title("Streamlit new chat elements")

# with st.chat_message("user"):
#     st.write("Hello 👋")

# with st.chat_message("assistant"):
#     st.write("Hello 👋 I'm assistant")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

def load_pdf_data(uploaded_file):
    pdf = PdfReader(uploaded_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

if uploaded_files is not None:
    st.write("File uploaded")
    for uploaded_file in uploaded_files:
        st.markdown(load_pdf_data(uploaded_file))