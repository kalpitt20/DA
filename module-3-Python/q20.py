# Q20: Mini bank management

balance = None
history = ""  # transactions stored in a string (no lists allowed)
while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance")
    print("5. Transaction History\n6. Exit")
    choice = input("Choose: ")
    if choice == "6":
        print("Goodbye!")
        break
    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice.")
        continue
    if choice == "1":
        if balance is not None:
            print("Account already exists.")
            continue
        amt = float(input("Initial balance: "))
        if amt < 0:
            print("Balance cannot be negative.")
            continue
        balance = amt
        history += f"Account opened: {amt}\n"
        print("Account created.")
        continue
    if balance is None:
        print("Create an account first (option 1).")
        continue
    if choice == "2":
        amt = float(input("Deposit amount: "))
        if amt <= 0:
            print("Amount must be positive.")
        else:
            balance += amt
            history += f"Deposit: {amt}\n"
            print("Deposited.")
    elif choice == "3":
        amt = float(input("Withdraw amount: "))
        if amt <= 0:
            print("Amount must be positive.")
        elif amt > balance:
            print("Insufficient balance.")
        else:
            balance -= amt
            history += f"Withdraw: {amt}\n"
            print("Withdrawn.")
    elif choice == "4":
        print("Balance:", balance)
    elif choice == "5":
        print("--- Transaction History ---")
        print(history if history != "" else "No transactions yet.")
