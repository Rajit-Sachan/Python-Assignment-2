# This program checks whether a given year is a leap year or not
# It also explains the reason based on the leap year rules

# asking the user to enter a year
input_year = int(input("Enter a year: "))

# checking leap year conditions step by step
if input_year % 400 == 0:
    leap_year_result = "Leap Year"
    reason_text = "Divisible by 400"

elif input_year % 100 == 0:
    leap_year_result = "NOT a Leap Year"
    reason_text = "Divisible by 100 but not by 400"

elif input_year % 4 == 0:
    leap_year_result = "Leap Year"
    reason_text = "Divisible by 4 and not by 100"

else:
    leap_year_result = "NOT a Leap Year"
    reason_text = "Not divisible by 4"

# printing result
print("\nYear:", input_year)
print("Result:", leap_year_result)
print("Reason:", reason_text)