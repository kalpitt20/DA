# Q9: ATM simulation

balance = 10000
while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        amt = float(input("Deposit amount: "))
        if amt > 0:
            balance += amt
            print("Deposited. New balance:", balance)
        else:
            print("Amount must be positive.")
    elif choice == "3":
        amt = float(input("Withdraw amount: "))
        if amt <= 0:
            print("Amount must be positive.")
        elif amt > balance:
            print("Insufficient balance.")
        else:
            balance -= amt
            print("Withdrawn. New balance:", balance)
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
