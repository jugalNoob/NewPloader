
import streamlit as st

st.title("machine learing project")

st.image("py.jpg" ,caption="python backImage" , width=200 )

if st.checkbox("show/hide"):
    st.text("hi i am jugal sharma")

#Radio button

#redio
status=st.radio("What is status",('Active' , 'Inactive'))

if status is 'Active':

    st.success('Active')

else:
    
    st.warning("your in inavtive")



a = st.sidebar.radio('Select one:', [1, 2])



col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")


#Display interactive widgets

# Display interactive widgets
st.button('Click me')
# st.experimental_data_editor('Edit data', data)
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
# st.download_button('Download file', data)
# st.camera_input("Take a picture")
st.color_picker('Pick a color')

if st.button("download"):

    st.success("yes")

else:
    st.warning("No")
