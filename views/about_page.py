import streamlit as st

def about_page():
    st.title("🦷 Tooth Exchange Regulation Authority (TERA)")
    col1, col2 = st.columns(2)
    with col1:
        st.image("imgs/TERA.png", width=250)
    with col2:
        st.write("\n")
        st.write("\n")
        st.write("Tooth Exchange Regulation Authority (TERA) is the Tooth Fairy’s official company in charge of tooth collection, quality control, and data reporting. From baby teeth to enchanted molars, TERA carefully inspects and catalogs every tooth—with a bit of fairy dust!")
    st.write("")