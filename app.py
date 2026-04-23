import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Odisha CollegeHub", layout="wide")

def load_full_app():
    try:
        # Sari files load karna
        with open("index.html", "r", encoding='utf-8') as f: html = f.read()
        with open("styles.css", "r", encoding='utf-8') as f: css = f.read()
        with open("database.js", "r", encoding='utf-8') as f: db = f.read()
        with open("app.js", "r", encoding='utf-8') as f: js = f.read()
            
        # Sabko ek saath jodna (Database pehle aana chahiye)
        full_code = f"<style>{css}</style>{html}<script>{db}</script><script>{js}</script>"
        components.html(full_code, height=1200, scrolling=True)
    except Exception as e:
        st.error(f"Missing File: {e}")

load_full_app()
