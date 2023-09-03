# in streamlit 1.26.0 version, st.status() is added
# Insert a status container to display output from long-running tasks.

import streamlit as st
import time

st.title('Streamlit new function Status')

st.write('hello world')

with st.status("counting down", expanded=True) as status:
    for i in range(10, 0, -1):
        st.write(f"{i}...")
        time.sleep(1)
    status.update(label="Time is up", state="complete", expanded=False)

st.button('Rerun')