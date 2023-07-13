import streamlit as st
import openai
from langchain.llms import OpenAI
from langchain.text_splitter import CharactorTextSpliter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Build an Ask the Doc app

st.set_page_config(page_title="LangChain Ask the Doc", page_icon="🦜🔗", layout="wide")
st.title("LangChain Ask the Doc")

uploaded_file = st.file_uploader("Upload a pdf file", type="pdf")

st.write("This app needs OpenAI API key to work. Please enter your API key below \n\n the key should start with 'sk-'")
# api_key should not be visible to the user, it should be like *****
api_key = st.text_input("API Key", type="password")
openai.api_key = api_key

if uploaded_file is not None:
    st.write("File uploaded")