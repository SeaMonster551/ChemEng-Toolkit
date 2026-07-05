import streamlit as st

from views import home, unit_converter, ideal_gas, fluid_flow, heat_transfer

st.set_page_config(
    page_title="Chemical Engineering Toolkit",
    page_icon="⚗️",
    layout="wide",
)

st.sidebar.title("Chemical Engineering Toolkit")

page = st.sidebar.radio(
    "Modules",
    [
        "Home",
        "Unit Converter",
        "Ideal Gas Law",
        "Fluid Flow",
        "Heat Transfer",
    ]
)

if page == "Home":
    home.show()

elif page == "Unit Converter":
    unit_converter.show()

elif page == "Ideal Gas Law":
    ideal_gas.show()

elif page == "Fluid Flow":
    fluid_flow.show()

elif page == "Heat Transfer":
    heat_transfer.show()