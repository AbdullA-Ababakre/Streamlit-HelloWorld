import streamlit as st
import time

st.title("Toast Message")

st.toast('You can use emoji :sunglasses: in toast message')

time.sleep(0.5)

st.toast('''You can use LaTeX: 
        $$ X^2 $$
        ''')

time.sleep(0.5)

st.toast('''You can change text color 
        :red[Red] :blue[Blue] :green[Green] :orange[Orange]  :violet[Violet]
        ''')
