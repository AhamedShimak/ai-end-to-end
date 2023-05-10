import streamlit as st
from utils import generate_image,summerize

st.title("Mute baby")
st.header("Yeah! I can't speak :( but I can show ;)")

text=st.text_area("You can speak :)")

if st.button("Now you go!"):
    if not text:
        st.error("Don't be shy!!! just say")
    else:
        with st.spinner("summerizing....."):
            summary= summerize(text)
        with st.spinner("Hmmmm Lemme say... OOOOPS Show!!"):
            image= generate_image(summary)
        st.info(f"summery:{summary}")
        st.image(image)