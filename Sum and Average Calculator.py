# This program takes multiple numbers from the user
# Then it calculates sum, average, maximum and minimum

# asking how many numbers user wants to enter
total_numbers = int(input("How many numbers? "))

# creating an empty list to store numbers
numbers_list = []

# loop to take inputs one by one
for i in range(1, total_numbers + 1):
    user_number = float(input(f"Enter number {i}: "))
    numbers_list.append(user_number)  # adding number to list

# calculating sum
sum_of_numbers = sum(numbers_list)

# calculating average
average_value = sum_of_numbers / total_numbers

# finding maximum and minimum
maximum_number = max(numbers_list)
minimum_number = min(numbers_list)

# printing results
print("\nResults:")
print("Sum:", sum_of_numbers)
print("Average:", average_value)
print("Maximum:", maximum_number)
print("Minimum:", minimum_number)