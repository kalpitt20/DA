# Q2: Positive / Negative / Zero

pos = neg = zero = 0
for i in range(15):
    n = float(input(f"Enter number {i + 1}: "))
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1
print("Positive:", pos, "| Negative:", neg, "| Zero:", zero)
