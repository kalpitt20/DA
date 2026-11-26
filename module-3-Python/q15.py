# Q15: Primes in a range

start = int(input("Start: "))
end = int(input("End: "))
count = 0
for n in range(start, end + 1):
    if n < 2:
        continue
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(n, end=" ")
        count += 1
print("\nTotal primes:", count)

# ---------------- Level 4 ----------------
