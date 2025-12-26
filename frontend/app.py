import streamlit as st
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.append(PROJECT_ROOT)

from backend.translate_backend import translate_text

# ------------------------------
# UI SETUP
# ------------------------------
st.set_page_config(
    page_title="HacFy Translator",
    page_icon="🌍",
    layout="centered"
)

# ------------------------------
# Custom CSS for Industry UI
# ------------------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background-color: #0f172a;
    color: #e2e8f0;
}
.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0px 0px 12px #00000060;
    margin-top: 18px;
}
textarea {
    background: #0f172a !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# TITLE
# ------------------------------
st.markdown("<h1 style='text-align:center;color:#38bdf8;'>🌍 HacFy Language Translator</h1>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#94a3b8;'>Translate anything across multiple languages instantly.</p>", 
            unsafe_allow_html=True)

# ------------------------------
# MAIN CARD
# ------------------------------


text_input = st.text_area("Enter text to translate:", height=10)

languages = [
     "Kannada", "Hindi", "Telugu", "Tamil",
    "Malayalam", "Spanish", "German", "French",
    "Japanese", "Korean", "Arabic"
]

target_language = st.selectbox("Translate To:", languages)

if st.button("🌐 Translate", use_container_width=True):
    if not text_input.strip():
        st.error("Please enter some text.")
    else:
        with st.spinner("Translating..."):
            result = translate_text(text_input, target_language)
        st.subheader(" Translated Text:")
        st.write(result)


