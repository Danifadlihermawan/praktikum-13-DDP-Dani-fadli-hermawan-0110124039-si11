import streamlit as st 

st.title("Ini Halaman Dashboard!") 
st.session_state['Nabung']

jumlah=0
for sission in st.session_state['Nabung']: 
    jumlah += sission['Nominal'] 

st.write("Total nominal menabung sebesar", jumlah)