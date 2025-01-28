import streamlit as st
import streamlit_extras
import streamlit_extras.let_it_rain
from streamlit_extras.card import card




 
r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])
r3col1, r3col2, r3col3 = st.columns([1, 0.25, 1])




with r1col2:
    st.title("Punnett Squares",)

with r2col1:
    st.image('whiteapple.png', "Apple 1")

with r3col2:
    if st.button("Cross"):
     with r2col2:  
      gene = st.selectbox("Enter the Gene: ", ["Color", "Sweetness", "Spice Level"])
      

with r2col3:
    st.image('whiteapple.png', "Apple 2")



streamlit_extras.let_it_rain.rain('•', 20, falling_speed=5, animation_length="infinite")
card(title="Template", text="template")

