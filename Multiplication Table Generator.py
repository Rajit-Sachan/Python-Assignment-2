# This program prints the multiplication table for a number
# User enters the number and the range till which table should print

# taking inputs
input_number = int(input("Enter number: "))
table_range_end = int(input("Enter range (end): "))

print("\nMultiplication Table of", input_number)

# loop to print table
for i in range(1, table_range_end + 1):
    result = input_number * i
    print(f"{input_number} x {i} = {result}")

# This prints full multiplication tables from 1 to 10 in grid format

print("\n=== FULL MULTIPLICATION TABLE (1–10) ===\n")

for row in range(1, 11):  # numbers 1 to 10
    for column in range(1, 11):
        print(f"{row*column:4}", end="")  # spacing for alignment
    print()  # move to next line