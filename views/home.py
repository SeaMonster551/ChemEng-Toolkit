import streamlit as st

def show():
    st.title("Chemical Enineering Toolkit")
    st.write("""
             This project is a collection of engineering 
             calculators for chemical engineering students. 
             Select a module from the sidebar.
             """
    )

    st.subheader("Current modules:")

    st.markdown("""
                Unit Converter

    Ideal Gas Law

    Fluid Flow

    Heat Transfer
    """)
