import streamlit as st
from calculators.units import TEMPERATURE_UNITS, convert_temperature
def show():
    st.title("Unit Converter")

    category = st.selectbox(
        "Select a category",
        ["Temperature"]
    )

    if category == "Temperature":

        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox(
                "From Unit",
                TEMPERATURE_UNITS
            )
        with col2:
            to_unit = st.selectbox(
                "To Unit",
                TEMPERATURE_UNITS
            )
        value = st.number_input(
            "Enter value",
            value=0.0
        )

        if st.button("Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result} {to_unit}")