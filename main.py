import streamlit as st
import streamlit_extras
import streamlit_extras.let_it_rain
from streamlit_extras.card import card
import streamlit_extras.theme
import streamlit_shadcn_ui as ui
import streamlit_antd_components as sac



if 'show_card' not in st.session_state:
    st.session_state.show_card = False

r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])
r3col1, r3col2, r3col3 = st.columns([1, 0.25, 1])


####################################################


def cross_genotypes(palleles1, palleles2):
    if palleles1 == "" and palleles2 == "": 
      st.info("Please provide an input") 
    else:      
        box1 = palleles1[0] + palleles2[1]
        box2 = palleles1[1] + palleles2[0]
        box3 = palleles1[1] + palleles2[1]
        box4 = palleles1[0] + palleles2[0]
        if box1[0] == "s":
            if box1[1] == "S":
                box1 = box1[::-1]
            else:
                box1 = box1
        if box2[0] == "s":
            if box2[1] == "S":
                box2 = box2[::-1]
            else:
                box2 = box2
        if box3[0] == "s":
            if box3[1] == "S":
                box3 = box3[::-1]
            else:
                box3 = box3
        if box4[0] == "s":
            if box4[1] == "S":
                box4 = box4[::-1]
            else:
                box4 = box4
        col1, col2 = st.columns([0.25, 0.25])
        r2col1, r2col2 = st.columns([0.25, 0.25])
        with col1:
            if st.button(box1, key=f'butn_{box1}'):
                pass
        with col2:
            if st.button(box2, key=f'bitn_{box2}'):
                pass
        with r2col1:
            if st.button(box3, key=f'betn_{box3}'):
                pass
        with r2col2:
            if st.button(box4, key=f'batn_{box4}'):
                pass
                            

####################################################                  
                        











with r2col2:  
      gene = st.selectbox("Enter the Phenotype: ", ["Color", "Sweetness", "Spice Level"])
      alleles1 = st.text_input("Enter the first parents alleles. (Eg: 'Ss')").lstrip().rstrip()
      alleles2 = st.text_input("Enter the second parents alleles. (Eg: 'Ss')").lstrip().rstrip()


with r1col2:
    st.title("Punnett Squares",)

with r2col1:
    st.image('whiteapple.png', "Apple 1")

with r3col2:
    if st.button("Cross"):
        st.session_state.show_card = True

if st.session_state.show_card:
    card(title="Punnett Square", text="Box will be generated below")
    cross_genotypes(alleles1, alleles2)

with r2col3:
    st.image('whiteapple.png', "Apple 2")


streamlit_extras.let_it_rain.rain('•', 20, falling_speed=5, animation_length="infinite")




