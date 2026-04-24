import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import io

# 1. Page Configuration
st.set_page_config(
    page_title="Odisha CollegeHub",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Updated CSS
st.markdown("""
<style>
    .block-container {padding: 0rem !important; max-width: 100% !important;}
    header[data-testid="stHeader"] {display: none !important;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    iframe {display: block; width: 100vw !important; border: none;}
    .stApp {overflow: hidden;}
    
    /* Admin Panel Styling */
    .admin-box {
        padding: 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin: 10px;
    }
</style>
""", unsafe_allow_html=True)

def load_main_app():
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
        components.html(full_code, height=2500, scrolling=True)
    except Exception as e:
        st.error(f"Error loading files: {e}")

def admin_panel():
    st.sidebar.title("🔐 Admin Access")
    pwd = st.sidebar.text_input("Enter Password", type="password")
    
    if pwd == "Odisha@2026": # Aap ise change kar sakte hain
        st.sidebar.success("Logged In!")
        show_admin = st.sidebar.checkbox("Open Import Dashboard")
        
        if show_admin:
            st.title("Admin Dashboard - Bulk College Import")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("1. Download Template")
                # Blank CSV Template
                template_cols = ["college_name", "location", "stream", "annual_fees", "rating", "placement_record", "official_link"]
                df_template = pd.DataFrame(columns=template_cols)
                csv = df_template.to_csv(index=False)
                
                st.download_button(
                    label="📥 Download Blank CSV Template",
                    data=csv,
                    file_name="college_import_template.csv",
                    mime="text/csv"
                )
                st.info("Iss file ko Excel mein bhar kar upload karein.")

            with col2:
                st.subheader("2. Upload Filled Data")
                uploaded_file = st.file_uploader("Choose CSV File", type="csv")
                
                if uploaded_file is not None:
                    new_data = pd.read_csv(uploaded_file)
                    st.write("Preview of data:")
                    st.dataframe(new_data)
                    
                    if st.button("🚀 Final Import to Project"):
                        # Yahan aapka logic aayega (Jaise database.js update karna)
                        st.success(f"Successfully imported {len(new_data)} colleges!")
                        st.balloons()

    elif pwd != "":
        st.sidebar.error("Wrong Password")

if __name__ == "__main__":
    # Sidebar control for Admin
    admin_panel()
    
    # Main App Load
    load_main_app()
