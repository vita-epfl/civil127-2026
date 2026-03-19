import random

from lab6.marmotte_sweeper.ui import MarmotteSweeperUI

# Code to create an instance of MarmotteSweeperUI and start
# the game.
# Adjust difficulty by changing the grid size and number of marmottes.
# Adjust the cell_size depending on the screen resolution.

random.seed(2)  # for testing purpose
game = MarmotteSweeperUI(9, 9, 15, 64)
game.start()
