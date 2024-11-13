﻿import streamlit as st
import base64

tab = {"jeden": 99.99, "dwa": 88.99, "trzy": 77.99, "cztery": 66.99, "piec": 55.99}

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .st-emotion-cache-1r4qj8v {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

set_png_as_page_bg('assets/image.png')

st.header(" :rainbow[WELCOME]")
st.balloons()