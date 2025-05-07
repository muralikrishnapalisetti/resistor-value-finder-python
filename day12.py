# Easy Dictionary for Color Codes
color_digit = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
}

color_multiplier = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
    "green": 100000, "blue": 1000000, "violet": 10000000,
    "gray": 100000000, "white": 1000000000, "gold": 0.1, "silver": 0.01
}

color_tolerance = {
    "brown": "±1%", "red": "±2%", "green": "±0.5%", "blue": "±0.25%",
    "violet": "±0.1%", "gray": "±0.05%", "gold": "±5%", "silver": "±10%", "none": "±20%"
}


# Simple Function to Find Resistor Value
def find_resistor_value():
    print("🛠️ Welcome to Resistor Value Finder!")
    print("👉 Please type the 4 color bands one by one (example: red, violet, yellow, gold).")

    band1 = input("First band color: ").strip().lower()
    band2 = input("Second band color: ").strip().lower()
    band3 = input("Third band (multiplier) color: ").strip().lower()
    band4 = input("Fourth band (tolerance) color: ").strip().lower()

    # Check if the colors entered are valid
    if (band1 not in color_digit or
            band2 not in color_digit or
            band3 not in color_multiplier or
            band4 not in color_tolerance):
        print("❌ Oops! You entered an invalid color. Please try again carefully.")
        return

    # Calculate the resistance value
    first_number = color_digit[band1]
    second_number = color_digit[band2]
    multiplier = color_multiplier[band3]
    tolerance = color_tolerance[band4]

    resistance_value = (first_number * 10 + second_number) * multiplier

    # Make resistance more readable
    if resistance_value >= 1_000_000:
        readable_value = f"{resistance_value / 1_000_000} MΩ"
    elif resistance_value >= 1_000:
        readable_value = f"{resistance_value / 1_000} kΩ"
    else:
        readable_value = f"{resistance_value} Ω"

    # Show the final result
    print(f"\n🎯 Your Resistor Value is: {readable_value} {tolerance}")


# Let's Run It!
find_resistor_value()
