# Q4: Sum of digits

n = int(input("Enter an integer: "))
if n < 0:
    n = -n
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)
