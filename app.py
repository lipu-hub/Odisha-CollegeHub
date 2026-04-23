import streamlit as st
import streamlit.components.v1 as components

# Page Title
st.set_page_config(page_title="Odisha CollegeHub", layout="wide")

# Aapka HTML load karne ke liye
try:
    with open("index (2).html", "r", encoding='utf-8') as f:
        html_code = f.read()
        components.html(html_code, height=1000, scrolling=True)
except Exception as e:
    st.error(f"Error: {e}. Make sure 'index (2).html' is in the repository.")
