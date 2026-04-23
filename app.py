import streamlit as st
import streamlit.components.v1 as components
import os

# Page Configuration
st.set_page_config(page_title="Odisha CollegeHub", layout="wide")

def load_full_app():
    try:
        # Sari files ko read karna
        with open("index.html", "r", encoding='utf-8') as f:
            html_content = f.read()
        with open("styles.css", "r", encoding='utf-8') as f:
            css_content = f.read()
        with open("database.js", "r", encoding='utf-8') as f:
            db_content = f.read()
        with open("app.js", "r", encoding='utf-8') as f:
            js_content = f.read()

        # Final Code Assembly
        # Humne Database ko JS logic se pehle rakha hai taaki data availability error na aaye
        full_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>{css_content}</style>
        </head>
        <body>
            {html_content}
            <script>
                // Injecting Database first
                {db_content}
                
                // Injecting App Logic second
                {js_content}
            </script>
        </body>
        </html>
        """
        
        # Rendering the component
        components.html(full_code, height=1500, scrolling=True)

    except Exception as e:
        st.error(f"⚠️ File Loading Error: {e}")
        st.info("Ensure index.html, styles.css, database.js, and app.js are in the same folder as app.py")

if __name__ == "__main__":
    load_full_app()
