def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("🌡️ TEMPERATURE CONVERTER")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")

choice = input("Choose (1-3): ")

try:
    if choice == '1':
        c = float(input("Enter Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c):.1f}°F")
    elif choice == '2':
        c = float(input("Enter Celsius: "))
        print(f"{c}°C = {celsius_to_kelvin(c):.2f}K")
    elif choice == '3':
        f = float(input("Enter Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f):.1f}°C")
    else:
        print("❌ Invalid choice")
except ValueError:
    print("❌ Please enter a valid number")