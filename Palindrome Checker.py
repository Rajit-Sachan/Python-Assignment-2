# This program checks if a word or number is a palindrome
# Palindrome means it reads the same forward and backward
# It ignores case (capital or small letters)

# taking input from user
user_input = input("Enter word/number: ")

# converting to lowercase so case doesn't matter
original_text = user_input.lower()

# reversing the text using slicing
reversed_text = original_text[::-1]

# showing step-by-step verification
print("\nOriginal:", user_input)
print("Reversed:", reversed_text)

# checking if palindrome
if original_text == reversed_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")