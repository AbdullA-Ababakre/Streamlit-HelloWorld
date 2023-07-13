import streamlit as st
from langchain llms import OPENAI
from langchain textspilter import CharactorTextSpliter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Build an Ask the Doc app

