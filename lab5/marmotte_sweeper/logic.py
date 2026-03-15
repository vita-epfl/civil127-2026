from abc import ABC, abstractmethod
import enum
import random


class Cell(enum.Enum):
    UNREVEALED = 1
    REVEALED = 2
    MARMOTTE = 3
    FLAGGED = 4


type coord = tuple[int, int]


class Rand(ABC):
    @abstractmethod
    def randint(self, a: int, b: int) -> int:
        pass


class RealRand(Rand):
    def randint(self, a: int, b: int) -> int:
        return random.randint(a, b)


class MarmotteSweeper:
    """
    Class that handles the game state. The code tracks:
    - positions of all the marmottes
    - positions which have been revealed
    - positions which have been flagged
    - mark a cell as revealed
    - mark/unmark a cell as flag

    All coordinates are grid-based since this class only deals
    at the internal logic level and doesn't know anything about the UI.
    """

    def __init__(self, width: int, height: int, count_marmottes: int, rand: Rand):
        self.width = width
        self.height = height
        self.revealed: set[coord] = set()
        self.flagged: set[coord] = set()
        self.marmottes: set[coord] = set()
        while len(self.marmottes) < count_marmottes:
            x = rand.randint(0, width - 1)
            y = rand.randint(0, height - 1)
            self.marmottes.add((x, y))

    def cell(self, pos: coord) -> Cell:
        """
        Returns information about the cell at x, y
        """
        if pos in self.revealed:
            if pos in self.marmottes:
                return Cell.MARMOTTE
            else:
                return Cell.REVEALED
        if pos in self.flagged:
            return Cell.FLAGGED
        return Cell.UNREVEALED

    def flag(self, pos: coord) -> None:
        """
        Toggle flag at x, y.
        x, y are grid coordinates.
        """
        if pos in self.flagged:
            self.flagged.remove(pos)
        else:
            self.flagged.add(pos)

    def reveal(self, pos: coord) -> None:
        """
        Reveal position (x, y).
        x, y are grid coordinates.
        """
        self.revealed.add(pos)
