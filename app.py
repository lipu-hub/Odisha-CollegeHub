import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Odisha CollegeHub", layout="wide")

def load_app():
    try:
        # Files ko sirf read karna hai
        with open("index.html", "r", encoding='utf-8') as f:
            html = f.read()
        with open("styles.css", "r", encoding='utf-8') as f:
            css = f.read()
        with open("database.js", "r", encoding='utf-8') as f:
            db = f.read()
        with open("app.js", "r", encoding='utf-8') as f:
            js = f.read()

        # Bina kisi extra text ke assemble karein
        full_code = f"<style>{css}</style>{html}<script>{db}</script><script>{js}</script>"
        
        components.html(full_code, height=1800, scrolling=True)
    except Exception as e:
        st.error(f"Error loading files: {e}")

if __name__ == "__main__":
    load_app()
