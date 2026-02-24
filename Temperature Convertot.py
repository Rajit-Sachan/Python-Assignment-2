# This program converts temperature between Celsius, Fahrenheit and Kelvin
# It uses a simple menu so the user can choose what conversion they want

while True:  # loop runs until user chooses exit

    # showing menu options
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    # asking user choice
    user_choice = int(input("Enter your choice (1-7): "))

    # option 1
    if user_choice == 1:
        celsius_value = float(input("Enter temperature in Celsius: "))
        fahrenheit_value = (celsius_value * 9/5) + 32
        print("Result:", round(fahrenheit_value, 2), "°F")

    # option 2
    elif user_choice == 2:
        fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
        celsius_value = (fahrenheit_value - 32) * 5/9
        print("Result:", round(celsius_value, 2), "°C")

    # option 3
    elif user_choice == 3:
        celsius_value = float(input("Enter temperature in Celsius: "))
        kelvin_value = celsius_value + 273.15
        print("Result:", round(kelvin_value, 2), "K")

    # option 4
    elif user_choice == 4:
        kelvin_value = float(input("Enter temperature in Kelvin: "))
        celsius_value = kelvin_value - 273.15
        print("Result:", round(celsius_value, 2), "°C")

    # option 5
    elif user_choice == 5:
        fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
        kelvin_value = (fahrenheit_value - 32) * 5/9 + 273.15
        print("Result:", round(kelvin_value, 2), "K")

    # option 6
    elif user_choice == 6:
        kelvin_value = float(input("Enter temperature in Kelvin: "))
        fahrenheit_value = (kelvin_value - 273.15) * 9/5 + 32
        print("Result:", round(fahrenheit_value, 2), "°F")

    # exit option
    elif user_choice == 7:
        print("Exiting program... 👋")
        break

    # if user enters invalid number
    else:
        print("Invalid choice, please try again.")