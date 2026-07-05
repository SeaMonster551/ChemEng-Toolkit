import streamlit as st
import calculators.units
st.write("Imported from:", __file__)
st.write("Categories:", calculators.units.UNIT_CATEGORIES)
def show():
    st.title("Unit Converter")


    category = st.selectbox(
        "Select a category",
        ["Temperature",
        calculators.units.UNIT_CATEGORIES.keys()
        ]
    )
    st.write(category)
    st.write(list(calculators.units.UNIT_CATEGORIES.keys()))

    if category == "Temperature":
        units = calculators.units.TEMPERATURE_UNITS
    
    else:
        units = list(calculators.units.UNIT_CATEGORIES[category].keys())

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
            result = calculators.units.convert_temperature(value, from_unit, to_unit)
        else:
            result = calculators.units.convert_units(value, from_unit, to_unit, calculators.units.UNIT_CATEGORIES[category])

        st.success(f"{value} {from_unit} = {result} {to_unit}")
        