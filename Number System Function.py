# This program contains multiple math-related functions
# A menu is provided to test each function

# ===== factorial =====
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# ===== prime check =====
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# ===== fibonacci =====
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b if n > 0 else 0

# ===== sum of digits =====
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# ===== reverse number =====
def reverse_number(n):
    return int(str(n)[::-1])

# ===== armstrong number =====
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

# ===== gcd =====
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# ===== lcm =====
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# ===== perfect number =====
def is_perfect_number(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# ===== menu =====
def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = int(input("Enter choice: "))

        if choice == 10:
            print("Exiting program 👋")
            break

        if choice in [1,2,3,4,5,6,9]:
            num = int(input("Enter number: "))

        if choice == 1:
            print("Factorial:", factorial(num))

        elif choice == 2:
            print("Prime:", is_prime(num))

        elif choice == 3:
            print("Fibonacci:", fibonacci(num))

        elif choice == 4:
            print("Sum of digits:", sum_of_digits(num))

        elif choice == 5:
            print("Reversed:", reverse_number(num))

        elif choice == 6:
            print("Armstrong:", is_armstrong(num))

        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == 9:
            print("Perfect Number:", is_perfect_number(num))

        else:
            print("Invalid choice")

# run menu
math_menu()
