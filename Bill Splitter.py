# This program helps split a restaurant bill between people
# It calculates tax, tip, total amount and how much each person should pay

# taking inputs from the user
total_bill_amount = float(input("Enter total bill: "))
number_of_people = int(input("Number of people: "))
tax_percentage = float(input("Tax percentage: "))
tip_percentage = float(input("Tip percentage: "))

# subtotal is the original bill
subtotal_amount = total_bill_amount

# calculating tax amount
tax_amount = (subtotal_amount * tax_percentage) / 100

# bill after adding tax
bill_after_tax = subtotal_amount + tax_amount

# calculating tip on the taxed bill
tip_amount = (bill_after_tax * tip_percentage) / 100

# final total bill
final_total_bill = bill_after_tax + tip_amount

# amount each person has to pay
amount_per_person = final_total_bill / number_of_people

# displaying results
print("\n=== BILL BREAKDOWN ===")
print(f"Subtotal: ₹{subtotal_amount:.2f}")
print(f"Tax ({tax_percentage}%): ₹{tax_amount:.2f}")
print(f"After tax: ₹{bill_after_tax:.2f}")
print(f"Tip ({tip_percentage}%): ₹{tip_amount:.2f}")
print(f"Total: ₹{final_total_bill:.2f}")
print(f"Per person: ₹{amount_per_person:.2f}")