import streamlit as st

# Set page configuration
st.set_page_config(page_title="HTML Viewer", layout="centered")

# Read the HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display the HTML
st.markdown(html_content, unsafe_allow_html=True)
