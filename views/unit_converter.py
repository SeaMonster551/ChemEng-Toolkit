import streamlit as st
from calculators.units import PRESSURE_UNITS, TEMPERATURE_UNITS, convert_temperature, convert_units
def show():
    st.title("Unit Converter")

    category = st.selectbox(
        "Select a category",
        [
            "Temperature",
            "Pressure"
            ]
    )

    if category == "Temperature":
        units = TEMPERATURE_UNITS
    
    elif category == "Pressure":
        units = PRESSURE_UNITS

    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From Unit",units)
    
    with col2:
        to_unit = st.selectbox("To Unit",units)
        
    value = st.number_input(
        "Enter value",
        value=0.0,
        step=0.01,
    )

    if st.button("Convert"):
        
        if category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result} {to_unit}")
        
        elif category == "Pressure":
            result = convert_units(value, from_unit, to_unit, PRESSURE_UNITS)
            st.success(f"{value} {from_unit} = {result} {to_unit}")