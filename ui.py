import streamlit as st
from boxesdraw import *
st.write("DigiFormAnalyser")
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("Filename", uploaded_file.name)
    csv_filename = makecsvandboxes(uploaded_file.name)
    
