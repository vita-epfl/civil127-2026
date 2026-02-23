import random


sum = 0
N = 1_000_000
for i in range(N):
    moves = 0
    marker = 1
    while marker != 100:
        # roll the dice and update marker
        dice = random.randint(1, 6)
        marker += dice
        moves += 1

        # handle bounce at 100
        if marker > 100:
            overflow = marker - 100
            marker = 100 - overflow

        # handle snakes and ladders
        if marker == 43:
            marker = 17
        elif marker == 50:
            marker = 5
        elif marker == 56:
            marker = 8
        elif marker == 73:
            marker = 15
        elif marker == 84:
            marker = 63
        elif marker == 87:
            marker = 49
        elif marker == 98:
            marker = 40
        elif marker == 2:
            marker = 23
        elif marker == 6:
            marker = 45
        elif marker == 20:
            marker = 59
        elif marker == 52:
            marker = 72
        elif marker == 57:
            marker = 96
        elif marker == 71:
            marker = 92

    sum += moves


average = sum / N
print("average:", average)
