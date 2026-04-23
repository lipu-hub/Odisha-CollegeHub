
import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration - Layout Wide hona zaroori hai
st.set_page_config(
    page_title="Odisha CollegeHub",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Side Gaps aur Padding hatane ke liye CSS
st.markdown("""
    <style>
        /* Main Streamlit container ki padding hatana */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        
        /* Header aur Padding top ko adjust karna */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        
        /* Iframe ko screen ke edge tak stretch karna */
        iframe {
            display: block;
            width: 100vw !important;
            border: none;
        }
        
        /* Extra white space niche se hatane ke liye */
        .stApp {
            overflow: hidden;
        }
    </style>
    """, unsafe_allow_html=True)

def load_app():
    try:
        # Files read karna
        with open("index.html", "r", encoding='utf-8') as f:
            html = f.read()
        with open("styles.css", "r", encoding='utf-8') as f:
            css = f.read()
        with open("database.js", "r", encoding='utf-8') as f:
            db = f.read()
        with open("app.js", "r", encoding='utf-8') as f:
            js = f.read()

        # Saare codes ko combine karna
        # meta charset UTF-8 add kiya hai taaki font aur symbols sahi dikhen
        full_code = f"""
        <!DOCTYPE html>
        <html style="margin:0; padding:0; width:100%;">
        <head>
            <meta charset="UTF-8">
            <style>{css}</style>
        </head>
        <body style="margin:0; padding:0; width:100%;">
            {html}
            <script>{db}</script>
            <script>{js}</script>
        </body>
        </html>
        """
        
        # Component ko render karna (Full Width Stretch)
        components.html(full_code, height=2000, scrolling=True)
        
    except Exception as e:
        st.error(f"Error loading files: {e}")

if __name__ == "__main__":
    load_app()
