# This program simulates a basic ATM
# It lets the user check balance, deposit money, withdraw money, or exit

# initial balance set to 10,000
account_balance = 10000

# loop runs until user chooses exit
while True:

    # showing ATM menu
    print("\n=== ATM SIMULATOR ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    user_choice = int(input("Enter choice: "))

    # option 1 → check balance
    if user_choice == 1:
        print("Current balance: ₹", account_balance)

    # option 2 → deposit money
    elif user_choice == 2:
        deposit_amount = float(input("Enter amount to deposit: "))
        account_balance += deposit_amount
        print("Deposit successful!")
        print("New balance: ₹", account_balance)

    # option 3 → withdraw money
    elif user_choice == 3:
        withdraw_amount = float(input("Enter amount to withdraw: "))

        # checking if enough balance remains (minimum 500 rule)
        if withdraw_amount > account_balance:
            print("Insufficient balance!")

        elif account_balance - withdraw_amount < 500:
            print("Cannot withdraw! Minimum ₹500 must remain in account.")

        else:
            account_balance -= withdraw_amount
            print("Withdrawal successful!")
            print("New balance: ₹", account_balance)

    # option 4 → exit
    elif user_choice == 4:
        print("Thank you for using ATM 👋")
        break

    # invalid option
    else:
        print("Invalid choice, please try again.")