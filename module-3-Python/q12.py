# Q12: Armstrong number

n = int(input("Enter a number: "))
digits = 0
temp = n
while temp > 0:
    digits += 1
    temp //= 10
total = 0
temp = n
while temp > 0:
    total += (temp % 10) ** digits
    temp //= 10
print("Armstrong Number" if total == n and n > 0 else "Not an Armstrong Number")
