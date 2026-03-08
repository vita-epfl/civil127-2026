# Battleship generator (4.2, part 1+2)
# Uses a dict for the grid
# see https://github.com/vita-epfl/civil127-2026/blob/main/lab4/lab4.pdf

import random

type coord = tuple[int, int]


class Battleship:
    """
    Represents one battleship board.
    Enables randomly placing ships on the grid and printing
    the grid.
    Enables one-player play.
    """

    COLS = "ABCDEFGHIJKLM"  # constant defined at the class level
    ROWS = "123456789"

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: dict[coord, str] = {}
        self.shots: set[coord] = set()

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
        self.ships = {
            "a": (5, "carrier"),
            "b": (4, "batteship"),
            "c": (3, "cruiser"),
            "d": (3, "submarine"),
            "e": (2, "destroyer"),
        }
        for ship, (length, _) in self.ships.items():
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
            print(Battleship.COLS[i], end=" ")
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

    def print_grid_with_shots(self):
        """
        Prints the grid with the shots


        Note: there's some code duplication between the two printing methods.
        It might make sense to merge them or refactor the common parts.
        """

        print("\033c")  # clear screen

        # print top header
        print(" ", end=" ")
        for i in range(0, self.width):
            print(Battleship.COLS[i], end=" ")
        print()

        for y in range(0, self.height):
            # print letter for each row
            print(y+1, end=" ")
            for x in range(0, self.width):
                if (x, y) in self.shots:
                    if (x, y) in self.grid:
                        print("#", end=" ")
                    else:
                        print("~", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

    def play(self) -> None:
        """
        Game loop. Prompts for input (in the form of <A-M letter><1-9 number>)
        until all the ships have been sunk.
        Assumes the grid has been initialized.
        """

        # Track which ships are left. Each ship starts with an integer equal to
        # its length. As the ship gets hit, the integer is decremented. When
        # the ship is sunk, it is removed from this data structure.
        # note: we assume you can't shoot in the same space twice.
        ships_hit: dict[str, int] = {}
        for ship, (length, _) in self.ships.items():
            ships_hit[ship] = length

        self.print_grid_with_shots()
        while len(ships_hit) > 0:
            s = input("target? ")

            # Check the input is valid
            if len(s) != 2:
                print("what?")
                continue
            if s[0] not in Battleship.COLS:
                print("what?")
                continue
            x = Battleship.COLS.index(s[0])

            if s[1] not in Battleship.ROWS:
                print("what?")
                continue
            y = Battleship.ROWS.index(s[1])

            if (x, y) in self.shots:
                print("You already fired here")
                continue

            # When we reach here, the (x, y) coordinates are valid
            self.shots.add((x, y))
            self.print_grid_with_shots()
            if (x, y) in self.grid:
                # we hit a ship
                ship = self.grid[(x, y)]
                ships_hit[ship] -= 1
                length, ship_name = self.ships[ship]
                if ships_hit[ship] == 0:
                    print("You sunk my", ship_name)
                    del ships_hit[ship]
                else:
                    print("You hit my", ship_name, "(", length, ")")
            else:
                print("Miss")
            print()
        print("You sunk all the things!")


game = Battleship(13, 9)
game.randomize_grid()
game.play()
