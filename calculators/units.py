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

LENGTH_UNITS = {
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.34,
    "km": 1000,
}

MASS_UNITS = {
    "kg": 1,
    "g": 0.001,
    "mg": 0.000001,
    "lb": 0.453592,
    "oz": 0.0283495,
}

VOLUME_UNITS = {
    "m³": 1,
    "L": 0.001,
    "mL": 1e-6,
    "cm³": 1e-6,
    "ft³": 0.0283168466,
    "in³": 1.6387064e-5,
    "gal (US)": 0.003785411784,
}

ENERGY_UNITS = {
    "J": 1,
    "kJ": 1000,
    "MJ": 1_000_000,
    "cal": 4.184,
    "kcal": 4184,
    "BTU": 1055.06,
    "kWh": 3_600_000,
}

POWER_UNITS = {
    "W": 1,
    "kW": 1000,
    "MW": 1_000_000,
    "hp": 745.7,
    "BTU/hr": 0.293071,
}

FORCE_UNITS = {
    "N": 1,
    "kN": 1000,
    "lbf": 4.448221615,
    "dyn": 1e-5,
}

TIME_UNITS = {
    "s": 1,
    "min": 60,
    "hr": 3600,
    "day": 86400,
}

AREA_UNITS = {
    "m²": 1,
    "cm²": 0.0001,
    "mm²": 1e-6,
    "ft²": 0.09290304,
    "in²": 0.00064516,
}

VELOCITY_UNITS = {
    "m/s": 1,
    "cm/s": 0.01,
    "ft/s": 0.3048,
    "km/hr": 0.277777778,
    "mph": 0.44704,
}

FLOWRATE_UNITS = {
    "m³/s": 1,
    "m³/hr": 1 / 3600,
    "L/s": 0.001,
    "L/min": 0.001 / 60,
    "L/hr": 0.001 / 3600,
    "gal/min": 0.003785411784 / 60,
    "ft³/min": 0.0283168466 / 60,
}

MASSFLOW_UNITS = {
    "kg/s": 1,
    "kg/hr": 1 / 3600,
    "g/s": 0.001,
    "lb/s": 0.45359237,
    "lb/hr": 0.45359237 / 3600,
}


DENSITY_UNITS = {
    "kg/m³": 1,
    "g/cm³": 1000,
    "lb/ft³": 16.018463,
}

VISCOSITY_UNITS = {
    "Pa·s": 1,
    "cP": 0.001,
    "mPa·s": 0.001,
}

UNIT_CATEGORIES = {
    "Pressure": PRESSURE_UNITS,
    "Length": LENGTH_UNITS,
    "Mass": MASS_UNITS,
    "Volume": VOLUME_UNITS,
    "Energy": ENERGY_UNITS,
    "Power": POWER_UNITS,
    "Force": FORCE_UNITS,
    "Time": TIME_UNITS,
    "Area": AREA_UNITS,
    "Velocity": VELOCITY_UNITS,
    "Flow Rate": FLOWRATE_UNITS,
    "Mass Flow": MASSFLOW_UNITS,
    "Density": DENSITY_UNITS,
    "Viscosity": VISCOSITY_UNITS,
}

def convert_units(value, from_unit, to_unit, unit_table):
    base_value = value * unit_table[from_unit]
    return base_value / unit_table[to_unit]
