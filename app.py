import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Odisha CollegeHub", layout="wide")

# Sabse simple tarika frontend load karne ka
try:
    with open("index.html", "r", encoding='utf-8') as f:
        html_data = f.read()
        components.html(html_data, height=1000, scrolling=True)
except Exception as e:
    st.error(f"Error: index.html nahi mil rahi. Please check file name on GitHub.")

st.sidebar.title("Vidya AI Status")
st.sidebar.success("App is Live! ✅")
