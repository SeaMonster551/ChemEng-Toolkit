"""Entry point for the ChemEng Toolkit application."""

from calculators.ideal_gas import ideal_gas_law


def main() -> None:
    """Print a simple startup message and a sample calculation."""
    sample = ideal_gas_law(1.0, 8.314, 298.0)
    print("ChemEng Toolkit is ready.")
    print(f"Example ideal gas result: {sample:.3f} Pa·m^3")


if __name__ == "__main__":
    main()
