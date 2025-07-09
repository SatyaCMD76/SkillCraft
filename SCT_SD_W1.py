def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_scale, to_scale):
    from_scale = from_scale.lower()
    to_scale = to_scale.lower()

    if from_scale == to_scale:
        return value

    if from_scale == "celsius":
        if to_scale == "fahrenheit":
            return celsius_to_fahrenheit(value)
        elif to_scale == "kelvin":
            return celsius_to_kelvin(value)

    elif from_scale == "fahrenheit":
        if to_scale == "celsius":
            return fahrenheit_to_celsius(value)
        elif to_scale == "kelvin":
            return fahrenheit_to_kelvin(value)

    elif from_scale == "kelvin":
        if to_scale == "celsius":
            return kelvin_to_celsius(value)
        elif to_scale == "fahrenheit":
            return kelvin_to_fahrenheit(value)

    raise ValueError("Invalid temperature scale provided.")

if __name__ == "__main__":
    print("Temperature Converter")
    temp = float(input("Enter temperature value: "))
    from_unit = input("Convert from (Celsius, Fahrenheit, Kelvin): ").strip()
    to_unit = input("Convert to (Celsius, Fahrenheit, Kelvin): ").strip()

    try:
        result = convert_temperature(temp, from_unit, to_unit)
        print(f"{temp} {from_unit.capitalize()} = {result:.2f} {to_unit.capitalize()}")
    except ValueError as ve:
        print("Error:", ve)
