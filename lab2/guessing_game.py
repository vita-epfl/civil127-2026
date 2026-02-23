# One-player number guessing game.
# Computer picks a number.
# Player keeps guessing. The program tells them if
# their number is too small, too big, or correct.

import random

secret = random.randint(1, 100)

attempts = 0
done = False
while not done:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret:
        print("Too small, try again")
    elif guess > secret:
        print("Too big, try again")
    else:
        print("You got it! Your score:", attempts)
        done = True
