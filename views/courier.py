import streamlit as st
import pandas as pd

def courier():
    st.title("🦷 Courier Analysis")
    # Upload file
    data = st.file_uploader("⏫ Upload a File to Analyze", type=["xlsx"])
    if data is not None:
        # Read file
        df = pd.read_excel(data)
        # Display data
        st.write(df)
        st.title("🔍 Information about your Data:")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Delivery Methods Found:")
            st.dataframe(df["Delivery Method"].unique())
        with col2:    
            st.write("Delivery Method Counts:")
            st.dataframe(df["Delivery Method"].value_counts())