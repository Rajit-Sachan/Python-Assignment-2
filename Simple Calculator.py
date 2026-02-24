                                            #Simple Calculator


first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

addition_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
division_result = first_number / second_number
modulus_result = first_number % second_number
exponentiation_result = first_number ** second_number

print("\nResults:")

print(f"{first_number} + {second_number} = {addition_result}")  # add
print(f"{first_number} - {second_number} = {subtraction_result}")  # subtract
print(f"{first_number} * {second_number} = {multiplication_result}")  # multiply
print(f"{first_number} / {second_number} = {round(division_result, 2)}")  # divide
print(f"{first_number} % {second_number} = {modulus_result}")  # mod
print(f"{first_number} ^ {second_number} = {exponentiation_result}")  # power
