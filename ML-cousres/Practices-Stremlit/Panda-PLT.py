# streamlit run your_script.py
# https://docs.streamlit.io/library/cheatsheet

import streamlit as st
import pandas  as pd

import matplotlib.pyplot as plt

st.success("jhhkj")

ff=pd.read_csv("friend.csv")

st.write(ff)



fig, ax = plt.subplots()
ax.bar(ff["name"], ff['marks'], linestyle='dotted', label='info' ,color = "#4CAF50") 
ax.set_xlabel("days")
ax.set_ylabel("stocks")
ax.set_title("s,j")
ax.grid()
ax.legend(loc=3)

st.pyplot(fig)


