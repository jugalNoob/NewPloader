# streamlit run your_script.py
# https://docs.streamlit.io/library/cheatsheet

import streamlit as st

#Title

st.title("machine project")

st.header("this is header")

st.subheader("this suharder")

st.text("s.kxjnjl")

st.write("python world") #bold text show

st.markdown("# this is markdow")
st.code('for i in range(8): foo()')
st.success("don jugal sharm")
st.info("sxkjhn")
st.warning("jugal this red code")
# st.image('./py.jpg')

st.exception("Name('name is not defined')")

# //Help panda as 
# import pandas 
# st.help(pandas)

# st.help(range)



## text super function 

st.write("text with ")
st.write(range(10))

#sideBar

st.sidebar.header("about")
st.sidebar.text("hey...")

# import time

# with st.spinner("ait a second"):
#     time.sleep(5)
#     st.success("scuuecc")

#     #ballons

# st.balloons()



# Tabs
# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")



# with st.form(key='my_form'):
#  username = st.text_input('Username')
#  password = st.text_input('Password')
#  st.form_submit_button('Login')



st.json({"name":"jugal" , "roll":"312"})



gamil=st.text_input("Enter your gmail id")

if '@gmail' in gamil:

    st.success(f"confrim your gamil id{gamil}")

loc=st.multiselect("where did you live" , ('indian' , 'usa' , 'Canda' , 'bangladesh'))
st.write("you Selection" , len(loc),'loc')


import datetime

st.date_input("today is" , datetime.datetime.now())

#time

import time
st.time_input("time is " , datetime.time())


with st.echo():
#how to import stremlit in your python script
  import streamlit



  #input dada inpute butteom


  first_name=st.text_input("enter your name")

  if st.button("submit" , key=1): #
     
     result=first_name.title()#
     st.success(result)#


import time

my_bar=st.progress(0)
for p in range(25):
   my_bar.progress(p +25)