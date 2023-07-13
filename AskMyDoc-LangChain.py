import streamlit as st
from langchain llms import OPENAI
from langchain textspilter import CharactorTextSpliter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Build an Ask the Doc app

st.set_page_config(page_title="LangChain Ask the Doc", page_icon="🦜🔗", layout="wide")
st.title("LangChain Ask the Doc")

uploaded_file = st.file_uploader("Upload a pdf file", type="pdf")
if uploaded_file is not None:
    st.write("File uploaded")