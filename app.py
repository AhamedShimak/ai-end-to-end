import streamlit as st
from utils import generate_image,summerize


st.set_page_config(initial_sidebar_state="collapsed")
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.title("Mute baby")

st.sidebar.header("Yeah! I can't speak....but I can show ")

text=st.sidebar.text_area("You can speak :)")

if st.sidebar.button("Now you go!"):
    if not text:
        st.error("Don't be shy!!! just say")
    else:
        with st.spinner("summerizing....."):
            summary= summerize(text)
        with st.spinner("Hmmmm Lemme say... OOOOPS Show!!"):
            image= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgWy3DLSoDNZxaoOiVo3G9I7-fXtRAztlpB8YtYejl&s"
        st.sidebar.info(f"summery:{summary}")
        st.sidebar.image(image) 
    
st.markdown('''
## Set of Images
'''
)
col1,col2,col3=st.columns(3)
with col1:
    st.markdown('''
#### Car
'''
)
    st.image("https://static.streamlit.io/examples/cat.jpg")
                
with col2:
    st.markdown('''
#### Three wheeler
'''
)
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
    with tab1:
        st.write("##### A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.write("##### A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.write("##### An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with col3:
    st.markdown('''
#### Three wheeler
'''
)
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.image(uploaded_file)