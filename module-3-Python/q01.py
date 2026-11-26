# Q1: Even or Odd Counter

even = 0
odd = 0
for i in range(10):
    n = int(input(f"Enter number {i + 1}: "))
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "| Odd:", odd)
