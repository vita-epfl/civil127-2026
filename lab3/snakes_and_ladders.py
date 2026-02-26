# Simulate lots of Snakes & Ladders games and calculate average
# number of moves per game.
# Short implementation, using dict.

import random

snakes_and_ladders = {
    43:  17, 50:  5, 56:  8, 73:  15, 84:  63, 87:  49, 98:  40,
    2:  23, 6:  45, 20:  59, 52:  72, 57:  96, 71:  92, 101: 99,
    102: 40, 103: 97, 104: 96, 105: 95,
}
moves = 0
N = 1_000_000

for i in range(N):
    marker = 1
    while marker != 100:
        marker += random.randint(1, 6)
        moves += 1
        marker = snakes_and_ladders.get(marker, marker)

print("average: ", moves / N)
