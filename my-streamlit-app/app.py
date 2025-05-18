import streamlit as st
import streamlit.components.v1 as components
import os

# Utility function to read files safely
def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        st.error(f"🚫 File not found: {path}")
        return ""

# Read HTML, CSS, JS
html = read_file("index.html")
css = f"<style>{read_file('style.css')}</style>"
js = f"<script>{read_file('main.js')}</script>"

# Show content
components.html(css + html + js, height=800, scrolling=True)
