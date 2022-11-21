# Temperature converter Celsius into F and F into Celsius.
# formula of conversion
# T(°Fahrenheit)=(T(°Celsius)*9/5)+32
version = "0.0.0.2"
print("Welcome on the Temp Converter \nDeveloped by : Noxious")
print("Temp Converter version: " + version)
print("Option 1 - Convert from Celsius to Fahrenheit")
print("Option 2 - Convert from Fahrenheit to Celsius")
option = input("Choose an option - 1 or 2:")

if option == "1":
    C = input("Type your temperature in Celsius: ")
    F = (float(C) * 9 / 5) + 32
    print("Temperature: " + str(F) + "degrees Fahrenheit")
elif option == "2":
    F = input("Type your temperature in Fahrenheit: ")
    C = (float(F) - 32) * 5 / 9
    print("Temperature: " + str(C) + "degrees Celsius")
else:
    print("Invalid option !")
