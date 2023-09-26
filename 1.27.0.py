import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write(st.__version__)

np.random.seed(42)
#using st.altair_chart 
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)

#using st.scatter_chart

st.scatter_chart(data=chart_data, x="a", y="b", size="c", color="c")

from vega_datasets import data

source = data.cars()
chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

st.altair_chart(chart, theme="streamlit", use_container_width=True)

st.scatter_chart(source, x="Horsepower", y="Miles_per_Gallon", color="Origin")