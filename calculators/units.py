TEMPERATURE_UNITS = [
    "Celsius (°C)",
    "Fahrenheit (°F)",
    "Kelvin (K)",
]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert from the source unit to Celsius
    if from_unit == "Celsius (°C)":
        celsius = value
    elif from_unit == "Fahrenheit (°F)":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin (K)":
        celsius = value - 273.15

    # Convert from Celsius to the target unit
    if to_unit == "Celsius (°C)":
        return celsius
    elif to_unit == "Fahrenheit (°F)":
        return celsius * 9 / 5 + 32
    elif to_unit == "Kelvin (K)":
        return celsius + 273.15

PRESSURE_UNITS = {
    "Pa": 1,
    "kPa": 1000,
    "MPa": 1000000,
    "bar": 100000,
    "atm": 101325,
    "psi": 6894.76,
    "torr": 133.322,
}
