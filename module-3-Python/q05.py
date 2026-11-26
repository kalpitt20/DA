# Q5: Number guessing game

secret = 42
while True:
    guess = int(input("Guess the number: "))
    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct! You guessed it.")
        break

# ---------------- Level 2 ----------------
