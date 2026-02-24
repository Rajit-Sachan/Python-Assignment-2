# This program first checks if a single number is prime
# Then it finds all prime numbers in a given range

# ===== PART 1: Single number check =====
input_number = int(input("Enter a number: "))

# handling special cases
if input_number <= 1:
    print(input_number, "is NOT a prime number")

else:
    is_prime = True  # assume number is prime

    # checking divisibility from 2 to number-1
    for i in range(2, input_number):
        if input_number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(input_number, "is a PRIME number")
    else:
        print(input_number, "is NOT a prime number")


# ===== PART 2: Prime numbers in a range =====
start_range = int(input("\nEnter start range: "))
end_range = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for num in range(start_range, end_range + 1):

    if num <= 1:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")