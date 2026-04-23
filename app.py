import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Odisha CollegeHub",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Updated CSS to bring back Navbar
st.markdown("""
    <style>
        /* Streamlit ki default padding hatana */
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        
        /* Streamlit ke default header/footer ko hatana */
        header[data-testid="stHeader"] {
            display: none !important;
        }
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        
        /* Iframe settings */
        iframe {
            display: block;
            width: 100vw !important;
            border: none;
        }

        /* Taaki scrollbar sahi se kaam kare */
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

        # HTML Assembly
        full_code = f"""
        <!DOCTYPE html>
        <html lang="en" style="margin:0; padding:0;">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>{css}</style>
        </head>
        <body style="margin:0; padding:0;">
            {html}
            <script>{db}</script>
            <script>{js}</script>
        </body>
        </html>
        """
        
        # Component Height check karein (Aapki site badi hai isliye 2500 suitable hai)
        components.html(full_code, height=2500, scrolling=True)
        
    except Exception as e:
        st.error(f"Error loading files: {e}")

if __name__ == "__main__":
    load_app()
