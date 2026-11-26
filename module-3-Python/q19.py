# Q19: Shopping billing

total = 0
while True:
    print("\n1. Rice  - Rs.60\n2. Oil   - Rs.150\n3. Sugar - Rs.45")
    print("4. Tea   - Rs.250\n5. Soap  - Rs.40\n0. Checkout")
    choice = input("Select product: ")
    if choice == "0":
        break
    if choice == "1":
        price = 60
    elif choice == "2":
        price = 150
    elif choice == "3":
        price = 45
    elif choice == "4":
        price = 250
    elif choice == "5":
        price = 40
    else:
        print("Invalid product.")
        continue
    qty = int(input("Quantity: "))
    if qty <= 0:
        print("Quantity must be positive.")
        continue
    total += price * qty
    print("Running total:", total)

if total < 1000:
    rate = 0
elif total < 5000:
    rate = 5
elif total < 10000:
    rate = 10
else:
    rate = 20
discount = total * rate / 100
print("\nBill:", total, "| Discount:", rate, "% =", discount)
print("Final amount: Rs.", total - discount)
