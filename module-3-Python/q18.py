# Q18: Second largest (distinct)

largest = int(input("Enter number 1: "))
second = None
for i in range(2, 11):
    x = int(input(f"Enter number {i}: "))
    if x > largest:
        second = largest
        largest = x
    elif x != largest and (second is None or x > second):
        second = x
print("Largest:", largest)
if second is None:
    print("No second largest (all numbers are equal).")
else:
    print("Second largest:", second)
