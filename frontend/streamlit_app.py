import streamlit as st

from sidebar import sidebar
from upload_page import upload_page
from chat_page import chat_page


st.set_page_config(
    page_title="AI PDF Assistant",
    page_icon="📄",
    layout="wide"
)

sidebar()

st.title("📄 AI PDF Assistant")

upload_page()

st.divider()

chat_page()
