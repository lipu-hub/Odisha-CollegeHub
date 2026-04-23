import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Odisha CollegeHub", layout="wide")

# CSS aur HTML ko ek saath load karne ka function
def load_app():
    try:
        with open("styles.css", "r", encoding='utf-8') as f:
            css_code = f.read()
        with open("index.html", "r", encoding='utf-8') as f:
            html_code = f.read()
        
        # HTML ke andar CSS inject karna
        full_code = f"<style>{css_code}</style>{html_code}"
        components.html(full_code, height=1000, scrolling=True)
    except Exception as e:
        st.error(f"Error: Files missing! Make sure index.html and styles.css are in the repo.")

load_app()

st.sidebar.success("Style Loaded! ✅")
