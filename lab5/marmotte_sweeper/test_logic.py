import unittest

from lab5.marmotte_sweeper.logic import Cell, Rand, MarmotteSweeper


class FakeRand(Rand):
    def __init__(self):
        self.i = 0

    def randint(self, a: int, b: int) -> int:
        self.i += 1
        return (self.i % (b - a + 1)) + a


class TestMarmotteSweeper(unittest.TestCase):
    def setUp(self) -> None:
        # 3x3 grid with Marmottes at 0,1 and 1,2
        # . . .
        # @ . .
        # . @ .
        self.marmotte_sweeper = MarmotteSweeper(3, 3, 2, FakeRand())

    def test_get_cell(self) -> None:
        self.assertEqual(Cell.UNREVEALED, self.marmotte_sweeper.cell((0, 0)))

    def test_flag(self) -> None:
        self.marmotte_sweeper.flag((0, 0))
        self.assertEqual(Cell.FLAGGED, self.marmotte_sweeper.cell((0, 0)))
        self.marmotte_sweeper.flag((0, 0))
        self.assertEqual(Cell.UNREVEALED, self.marmotte_sweeper.cell((0, 0)))

    def test_reveal(self) -> None:
        self.marmotte_sweeper.reveal((2, 0))
        self.assertEqual(Cell.REVEALED, self.marmotte_sweeper.cell((2, 0)))
        self.assertEqual(Cell.UNREVEALED, self.marmotte_sweeper.cell((1, 1)))


if __name__ == "__main__":
    unittest.main()
