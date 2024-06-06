def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Sample Inputs
celsius_temp = 25
fahrenheit_temp = 77

# Function Calls and Outputs
converted_to_fahrenheit = celsiusToFahrenheit(celsius_temp)
converted_to_celsius = fahrenheitToCelsius(fahrenheit_temp)

print(f"{celsius_temp}°C is {converted_to_fahrenheit}°F")
print(f"{fahrenheit_temp}°F is {converted_to_celsius}°C")
