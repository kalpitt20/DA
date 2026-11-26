# Q11: Palindrome number

n = int(input("Enter an integer: "))
original = n
if n < 0:
    print("Not a Palindrome")
else:
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    print("Palindrome" if rev == original else "Not a Palindrome")
