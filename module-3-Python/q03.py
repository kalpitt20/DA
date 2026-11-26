# Q3: Multiplication table

n = int(input("Enter a number: "))
total = 0
for i in range(1, 11):
    result = n * i
    print(n, "x", i, "=", result)
    total += result
print("Sum of all results:", total)
