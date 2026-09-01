"""Simple command-line unit converter."""


def convert_length(value, from_unit, to_unit):
    """Convert between meters, kilometers, miles, and feet."""
    # Convert the input value to meters first.
    to_meters = {
        "m": 1.0,
        "km": 1000.0,
        "mi": 1609.344,
        "ft": 0.3048,
    }
    # Convert from meters to the requested output unit.
    from_meters = {
        "m": 1.0,
        "km": 1 / 1000.0,
        "mi": 1 / 1609.344,
        "ft": 1 / 0.3048,
    }
    meters = value * to_meters[from_unit]
    return meters * from_meters[to_unit]


def convert_weight(value, from_unit, to_unit):
    """Convert between grams, kilograms, pounds, and ounces."""
    # Convert the input value to grams first.
    to_grams = {
        "g": 1.0,
        "kg": 1000.0,
        "lb": 453.59237,
        "oz": 28.349523125,
    }
    # Convert from grams to the requested output unit.
    from_grams = {
        "g": 1.0,
        "kg": 1 / 1000.0,
        "lb": 1 / 453.59237,
        "oz": 1 / 28.349523125,
    }
    grams = value * to_grams[from_unit]
    return grams * from_grams[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """Convert between Celsius, Fahrenheit, and Kelvin."""
    # If units are the same, no math is needed.
    if from_unit == to_unit:
        return value

    # Convert the input value to Celsius as a shared base.
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    else:  # from_unit == "k"
        celsius = value - 273.15

    # Convert from Celsius to the target unit.
    if to_unit == "c":
        return celsius
    if to_unit == "f":
        return (celsius * 9 / 5) + 32
    return celsius + 273.15  # to_unit == "k"


def choose_option(prompt, options):
    """Prompt until the user enters one of the allowed options."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"Invalid option. Choose one of: {', '.join(options)}")


def read_number(prompt):
    """Prompt until the user enters a valid number."""
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Please enter a valid number.")


def run_converter():
    """Run the main converter loop."""
    categories = {
        "length": ["m", "km", "mi", "ft"],
        "weight": ["g", "kg", "lb", "oz"],
        "temperature": ["c", "f", "k"],
    }

    print("Welcome to the Unit Converter!")

    # Keep looping so users can convert multiple values.
    while True:
        print("\nCategories: length, weight, temperature")
        category = choose_option("Choose a category: ", categories.keys())
        units = categories[category]

        print(f"Available units: {', '.join(units)}")
        from_unit = choose_option("Convert from: ", units)
        to_unit = choose_option("Convert to: ", units)
        value = read_number("Enter the value to convert: ")

        # Pick the correct conversion function by category.
        if category == "length":
            result = convert_length(value, from_unit, to_unit)
        elif category == "weight":
            result = convert_weight(value, from_unit, to_unit)
        else:
            result = convert_temperature(value, from_unit, to_unit)

        print(f"Result: {value} {from_unit} = {result:.4f} {to_unit}")

        again = choose_option("Convert another value? (y/n): ", ["y", "n"])
        if again == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    run_converter()
