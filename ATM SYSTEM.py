PIN = "1234"
balance = 1000
transaction_history = []


def check_balance():
    print("\nYour current balance is:", balance)


def deposit(amount):
    global balance
    balance += amount
    transaction_history.append(("Deposit", amount))
    print("\nAmount deposited: $", amount)
    print("Your new balance is: $", balance)


def withdraw(amount):
    global balance
    if amount > balance:
        print("\nInsufficient funds. Your current balance is: $", balance)
    else:
        balance -= amount
        transaction_history.append(("Withdrawal", amount))
        print("\nAmount withdrawn: $", amount)
        print("Your new balance is: $", balance)


def generate_mini_statement():
    print("\n----- Mini Statement -----")
    if len(transaction_history) == 0:
        print("No transactions found.")
    else:
        for transaction in transaction_history:
            print(transaction[0], "$", transaction[1])
    print("-------------------------")


def change_pin():
    global PIN
    new_pin = input("\nEnter a new PIN: ")
    confirm_pin = input("Confirm new PIN: ")
    if new_pin == confirm_pin:
        PIN = new_pin
        print("\nPIN successfully changed!")
    else:
        print("\nPIN change failed. PINs did not match.")


def exit_program():
    print("\nThank you for using this ATM. Goodbye!")


def run():
    print("\nWelcome to my ATM")
    pin_attempts = 0

    while pin_attempts < 3:
        pin_entry = input("\nPlease enter your PIN: ")
        if pin_entry == PIN:
            print("\nPIN Accepted")
            break
        else:
            pin_attempts += 1
            if pin_attempts == 3:
                print("\nToo many failed attempts. Your account has been locked.")
                return
            else:
                print("\nInvalid PIN. Please try again.")

    while True:
        print("\nWhat would you like to do?")
        print("1. Check account balance")
        print("2. Deposit funds")
        print("3. Withdraw funds")
        print("4. Generate mini statement")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("\nPlease enter your choice: ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            amount = float(input("\nEnter the amount to deposit: $"))
            deposit(amount)
        elif choice == "3":
            amount = float(input("\nEnter the amount to withdraw: $"))
            withdraw(amount)
        elif choice == "4":
            generate_mini_statement()
        elif choice == "5":
            change_pin()
        elif choice == "6":
            exit_program()
            break
        else:
            print("Invalid choice. Please try again.")


run()
