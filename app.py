import streamlit as st
import streamlit.components.v1 as components
import os

# Page Configuration
st.set_page_config(page_title="Odisha CollegeHub", layout="wide")

def load_full_app():
    try:
        # Sari files ko read karna
        with open("index.html", "r", encoding='utf-8') as f:
            html = f.read()
        with open("styles.css", "r", encoding='utf-8') as f:
            css = f.read()
        with open("app.js", "r", encoding='utf-8') as f:
            js = f.read()
            
        # CSS aur JS ko HTML ke andar integrate karna
        full_code = f"""
        <style>{css}</style>
        {html}
        <script>{js}</script>
        """
        
        # UI Render karna
        components.html(full_code, height=1200, scrolling=True)
        
    except Exception as e:
        st.error(f"⚠️ Error: Kuch files missing hain! {e}")

# Streamlit Sidebar Status
st.sidebar.title("Vidya AI Counselor")
if st.secrets.get("CLAUDE_API_KEY"):
    st.sidebar.success("API Connected ✅")
else:
    st.sidebar.warning("API Key Missing in Secrets ⚠️")

# Run App
load_full_app()
