# This program calculates total marks, percentage, grade and pass/fail result
# It asks the user to enter marks for 5 subjects

# taking marks input
subject1_marks = float(input("Enter marks for Subject 1: "))
subject2_marks = float(input("Enter marks for Subject 2: "))
subject3_marks = float(input("Enter marks for Subject 3: "))
subject4_marks = float(input("Enter marks for Subject 4: "))
subject5_marks = float(input("Enter marks for Subject 5: "))

# calculating total marks out of 500
total_marks = (
    subject1_marks +
    subject2_marks +
    subject3_marks +
    subject4_marks +
    subject5_marks
)

# calculating percentage
percentage = (total_marks / 500) * 100

# deciding grade based on percentage
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# checking pass or fail (must be >= 40 in all subjects)
if (
    subject1_marks >= 40 and
    subject2_marks >= 40 and
    subject3_marks >= 40 and
    subject4_marks >= 40 and
    subject5_marks >= 40
):
    result_status = "Pass"
else:
    result_status = "Fail"

# printing results
print("\n=== RESULT ===")
print("Marks:", subject1_marks, subject2_marks, subject3_marks, subject4_marks, subject5_marks)
print("Total Marks:", total_marks, "/ 500")
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
print("Result:", result_status)