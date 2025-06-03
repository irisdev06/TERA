import streamlit as st
import pandas as pd
from views.about_page import about_page
from views.courier import courier

# NAVIGATION SETUP 
st.sidebar.title("🖱 Navigation")
page = st.sidebar.selectbox("Choose Page", ["🕵🏽‍♀️ Info", "📩 Courier"])

# Show selected page
if page == "🕵🏽‍♀️ Info":
    about_page()
elif page == "📩 Courier":
    courier()