import unittest

from lab6.marmotte_sweeper.logic import Cell, Rand, MarmotteSweeper


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

    def test_count(self):
        self.assertEqual(1, self.marmotte_sweeper.count(1, 0))
        self.assertEqual(2, self.marmotte_sweeper.count(1, 1))
        self.assertEqual(0, self.marmotte_sweeper.count(2, 0))

    def test_in_bounds(self):
        self.assertTrue(self.marmotte_sweeper.in_bounds(0, 0))
        self.assertTrue(self.marmotte_sweeper.in_bounds(2, 2))
        self.assertFalse(self.marmotte_sweeper.in_bounds(-1, 0))
        self.assertFalse(self.marmotte_sweeper.in_bounds(0, -1))
        self.assertFalse(self.marmotte_sweeper.in_bounds(3, 1))
        self.assertFalse(self.marmotte_sweeper.in_bounds(1, 3))

    def test_reveal_recursive(self):
        self.marmotte_sweeper.reveal_recursive(2, 0)
        self.assertEqual(Cell.REVEALED, self.marmotte_sweeper.cell((2, 0)))
        self.assertEqual(Cell.REVEALED, self.marmotte_sweeper.cell((1, 1)))

    def test_reveal_iterative(self):
        self.marmotte_sweeper.reveal_iterative({(2, 0)})
        self.assertEqual(Cell.REVEALED, self.marmotte_sweeper.cell((2, 0)))
        self.assertEqual(Cell.REVEALED, self.marmotte_sweeper.cell((1, 1)))


if __name__ == "__main__":
    unittest.main()
