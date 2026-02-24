# This program calculates age using the exact birth date
# It gives a more accurate result compared to just using birth year

from datetime import datetime

# asking user to enter birth date step by step
birth_day = int(input("Enter birth day (1-31): "))
birth_month = int(input("Enter birth month (1-12): "))
birth_year = int(input("Enter birth year: "))

# creating a date object from user input
birth_date = datetime(birth_year, birth_month, birth_day)

# getting current date and time
current_date = datetime.now()

# finding the difference between today and birth date
age_difference = current_date - birth_date

# total days lived
total_days_lived = age_difference.days

# calculating age in different units
current_age_years = total_days_lived // 365
age_in_months = current_age_years * 12
age_in_hours = total_days_lived * 24
age_in_minutes = age_in_hours * 60

# calculating years left to reach 100
years_until_100 = 100 - current_age_years

# printing results
print("\nResults:")
print("Current age (approx years):", current_age_years)
print("Age in months (approx):", age_in_months)
print("Age in days:", total_days_lived)
print("Age in hours:", age_in_hours)
print("Age in minutes:", age_in_minutes)
print("Years until age 100:", years_until_100)