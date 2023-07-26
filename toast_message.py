import streamlit as st
import time

st.title("Toast Message")

if st.button('Try Emojis'):
    st.toast('You can use emoji :sunglasses: in toast message')

    time.sleep(0.5)

if st.button('Try LaTeX'):
    st.toast('''You can use LaTeX: 
            $$ X^2 $$
            ''')

    time.sleep(0.5)

if st.button('Try Colored Text'):
    st.toast('''You can change text color 
            :red[Red] :blue[Blue] :green[Green] :orange[Orange]  :violet[Violet]
            ''')
