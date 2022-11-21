# Temperature converter Celsius into F and F into Celsius.
# formula of conversion
# T(°Fahrenheit)=(T(°Celsius)*9/5)+32
version = "0.0.0.3"
print("Welcome on the Temp Converter \nDeveloped by : Noxious")
print("Temp Converter version: " + version)
while True:
    print("Option 1 - Convert from Celsius to Fahrenheit")
    print("Option 2 - Convert from Fahrenheit to Celsius")
    option = input("Choose an option - 1 or 2:")
    if option == "1":
        try:
            C = input("Type your temperature in Celsius: ")
            F = (float(C) * 9 / 5) + 32
            print("Temperature: " + str(F) + " degrees Fahrenheit")
        except ValueError:
            print("This is not an number , try again !")
    elif option == "2":
        try:
            F = input("Type your temperature in Fahrenheit: ")
            C = (float(F) - 32) * 5 / 9
            print("Temperature: " + str(C) + " degrees Celsius")
        except ValueError:
            print("This is not an number , try again !")
    else:
        print("Invalid option !")
