# Battleship generator (4.2, part 1)
# Uses a dict for the grid
# see https://github.com/vita-epfl/civil127-2026/blob/main/lab4/lab4.pdf

import random

type coord = tuple[int, int]


class Battleship:
    """
    Represents one battleship board.
    For now, enables randomly placing ships on the grid and printing
    the grid.
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: dict[coord, str] = {}

    def will_fit(self, length: int, pos: coord, dir: coord) -> bool:
        """
        Checks if a ship of given length will fit in the grid.


        dir must be either (1, 0) for horizontal ships or (0, 1) for vertical
        ships.
        """
        x, y = pos
        dx, dy = dir
        for i in range(length):
            if (x, y) in self.grid:
                # There's already a ship here
                return False
            if x == self.width or y == self.height:
                # We are going out of bounds
                return False
            x += dx
            y += dy
        return True

    def place(self, letter: str, length: int, pos: coord, dir: coord) -> None:
        """
        Places a ship on the grid. Assumes that the ship will fit.


        dir must be either (1, 0) for horizontal ships or (0, 1) for vertical
        ships.
        """
        x, y = pos
        dx, dy = dir
        for i in range(length):
            self.grid[(x, y)] = letter
            x += dx
            y += dy

    def randomize_grid(self) -> None:
        """
        Initialize the grid by randomly placing the ships.
        """
        ships = {
            "a": (5, "carrier"),
            "b": (4, "batteship"),
            "c": (3, "cruiser"),
            "d": (3, "submarine"),
            "e": (2, "destroyer"),
        }
        for ship, (length, _) in ships.items():
            ok = False
            while not ok:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                pos = (x, y)
                dir = random.choice([(1, 0), (0, 1)])
                if self.will_fit(length, pos, dir):
                    self.place(ship, length, pos, dir)
                    ok = True

    def print_grid_with_ships(self):
        """
        Prints the grid with the ships, useful for debugging
        """

        # print top header
        print(" ", end=" ")
        for i in range(0, self.width):
            print("ABCDEFGHIJKLM"[i], end=" ")
        print()

        for y in range(0, self.height):
            # print letter for each row
            print(y + 1, end=" ")
            for x in range(0, self.width):
                if (x, y) in self.grid:
                    print(self.grid[x, y], end=" ")
                else:
                    print(".", end=" ")
            print()


random.seed(94)
game = Battleship(13, 9)
game.randomize_grid()
game.print_grid_with_ships()
