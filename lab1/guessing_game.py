# Two-player number guessing game.
# Player 1 picks a number.
# Player 2 keeps guessing. The program tells them if
# their number is too small, too big, or correct.

print("\033c")  # clear the screen when the game starts
secret = input("player 1, pick a number between 1 and 100: ")
print("\033c")  # clear the screen so player 2 doesn't see player 1's input

attempts = 0

done = False
while not done:
    guess = input("player 2, enter your guess: ")
    attempts += 1
    # ASSUMPTION: `guess` and `secret` are numbers.
    if guess == secret:
        print("You got it! Your score:", attempts)
        done = True
    if guess < secret:
        print("Too small, try again")
    if guess > secret:
        print("Too big, try again")
