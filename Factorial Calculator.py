# This program calculates factorial of a number using a loop
# It also shows the step-by-step multiplication

# asking user to enter a number
input_number = int(input("Enter a number: "))

# checking for negative number
if input_number < 0:
    print("Factorial is not defined for negative numbers")

else:
    factorial_result = 1
    steps_text = ""  # to store steps like 5 x 4 x 3 ...

    # loop from number down to 1
    for i in range(input_number, 0, -1):
        factorial_result *= i
        steps_text += str(i)

        if i != 1:  # add x symbol except last
            steps_text += " x "

    # printing result
    print(f"{input_number}! = {steps_text} = {factorial_result}")