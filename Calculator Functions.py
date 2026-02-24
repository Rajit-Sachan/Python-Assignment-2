# This program is a calculator built using functions
# Each operation is written as a separate function

# ===== function for addition =====
def add(a, b):
    return a + b

# ===== function for subtraction =====
def subtract(a, b):
    return a - b

# ===== function for multiplication =====
def multiply(a, b):
    return a * b

# ===== function for division =====
def divide(a, b):
    if b == 0:  # handling division by zero
        return "Cannot divide by zero"
    return a / b

# ===== function for modulus =====
def modulus(a, b):
    return a % b

# ===== function for power =====
def power(a, b):
    return a ** b


# ===== main calculator function =====
def calculator():
    while True:
        print("\n=== FUNCTION CALCULATOR ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 7:
            print("Exiting calculator 👋")
            break

        # taking numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # calling functions based on choice
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = modulus(num1, num2)
        elif choice == 6:
            result = power(num1, num2)
        else:
            print("Invalid choice")
            continue

        print("Result:", result)


# calling the main function
calculator()