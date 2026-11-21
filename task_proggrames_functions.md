# list of programmes
**instructions**
**done all programmes take input from users and using user defined function don't used any inbuilt functions**


1. Function to add two numbers.
Ans.
def add_numbers(a, b):
    
    return a + b


x = int(input("Enter first number: "))

y = int(input("Enter second number: "))

print("Sum:", add_numbers(x, y))

Output:

Enter first number: 2

Enter second number: 3

Sum: 5


2. Function to find the largest of two numbers.

Ans.

def find_largest(a, b):

    if a > b:

        return a

    return b



x = int(input("Enter first number: "))

y = int(input("Enter second number: "))

print("Largest:", find_largest(x, y))

Output:

Enter first number: 3

Enter second number: 2

Largest: 3

3. Function to check whether a number is even or odd.

Ans.

def even_or_odd(n):

    if n % 2 == 0:

        return "Even"

    return "Odd"




num = int(input("Enter a number: "))

print("Number is:", even_or_odd(num))


Output:

Enter a number: 1

Number is: Odd

4. Function to find the factorial of a number.

Ans.

def get_factorial(n):

    if n < 0:

        return "Not defined for negative numbers"

    fact = 1

    i = 1

    while i <= n:

        fact = fact * i

        i = i + 1

    return fact


num = int(input("Enter a number: "))

print("Factorial:", get_factorial(num))

Output:

Enter a number: 4

Factorial: 24

5. Function to check whether a number is prime.

Ans.

def check_prime(n):

    if n <= 1:

        return False

    i = 2

    while i < n:

        if n % i == 0:

            return False

        i = i + 1

    return True


num = int(input("Enter a number: "))

if check_prime(num):

    print("Prime")

else:

    print("Not Prime")

Output:

Enter a number: 4

Not Prime

6. Function to reverse a number.

Ans.

def reverse_num(n):

    rev = 0

    while n > 0:

        last_digit = n % 10

        rev = rev * 10 + last_digit

        n = n // 10

    return rev



num = int(input("Enter a positive number: "))

print("Reversed:", reverse_num(num))

Output:

Enter a positive number: 23

Reversed: 32

7. Function to find the sum of digits of a number.

Ans.

def digit_sum(n):

    total = 0

    while n > 0:

        total = total + (n % 10)

        n = n // 10

    return total


num = int(input("Enter a positive number: "))

print("Sum of digits:", digit_sum(num))

Output:

Enter a positive number: 22

Sum of digits: 4

8. Function to check whether a string is a palindrome.

Ans.

def is_palindrome(text):

    rev_text = ""

    for ch in text:

        rev_text = ch + rev_text

    return text == rev_text



word = input("Enter a string: ")

if is_palindrome(word):

    print("Palindrome")

else:

    print("Not a Palindrome")

Output:

Enter a string: dad

Palindrome

9. Function to calculate the power of a number.

Ans.

def find_power(base, exp):

    ans = 1

    count = 0

    while count < exp:

        ans = ans * base

        count = count + 1

    return ans



b = float(input("Enter base: "))

e = int(input("Enter exponent (0 or positive): "))

print("Answer:", find_power(b, e))

Output:

Enter base: 2

Enter exponent (0 or positive): 3

Answer: 8.0

10. Function to find the Fibonacci series.

Ans.

def print_fibonacci(n):

    a = 0

    b = 1

    i = 0

    while i < n:

        print(a, end=" ")

        c = a + b

        a = b

        b = c

        i = i + 1

    print()



terms = int(input("Enter number of terms: "))

print_fibonacci(terms)



Output:

Enter number of terms: 10

0 1 1 2 3 5 8 13 21 34 

