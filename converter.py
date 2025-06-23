import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Create parser
parser = argparse.ArgumentParser(description="Temperature Converter (Celsius ↔ Fahrenheit)")

# Add arguments
parser.add_argument("value", type=float, help="Temperature value to convert")
parser.add_argument(
    "--to", choices=["C", "F"], required=True,
    help="Convert to: C (Celsius) or F (Fahrenheit)"
)

# Parse arguments
args = parser.parse_args()

# Perform conversion
if args.to == "F":
    result = celsius_to_fahrenheit(args.value)
    print(f"{args.value}°C = {result:.2f}°F")
else:
    result = fahrenheit_to_celsius(args.value)
    print(f"{args.value}°F = {result:.2f}°C")
