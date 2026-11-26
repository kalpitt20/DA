# Q7: Prime checker

n = int(input("Enter a number: "))
is_prime = n >= 2
i = 2
while i * i <= n:
    if n % i == 0:
        is_prime = False
        break
    i += 1
print("Prime" if is_prime else "Not Prime")
