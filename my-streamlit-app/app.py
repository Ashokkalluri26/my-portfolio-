import streamlit as st
import streamlit.components.v1 as components

# Load HTML from file
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Inject custom CSS
with open("style.css", "r", encoding="utf-8") as file:
    css = f"<style>{file.read()}</style>"

# Inject JavaScript
with open("script.js", "r", encoding="utf-8") as file:
    js = f"<script>{file.read()}</script>"

# Render the component
components.html(css + html_content + js, height=600, scrolling=True)
