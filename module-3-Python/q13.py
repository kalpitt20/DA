# Q13: Fibonacci

terms = int(input("Number of terms: "))
a, b = 0, 1
for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print()
