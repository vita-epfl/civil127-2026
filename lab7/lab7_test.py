import unittest

import lab7


class TestLab7(unittest.TestCase):
    def test_count_patterns(self):
        a = lab7.count_patterns(range(1000, 10000))
        self.assertEqual(a, (171, 4536, 3105))

    def test_has_three_consecutive(self):
        self.assertTrue(lab7.has_three_consecutive("122234"))
        self.assertFalse(lab7.has_three_consecutive("9322"))

    def test_are_all_different(self):
        self.assertTrue(lab7.are_all_different("92103"))
        self.assertFalse(lab7.are_all_different("71479"))

    def test_is_alternating(self):
        self.assertTrue(lab7.is_alternating("285609"))
        self.assertTrue(lab7.is_alternating("638342"))
        self.assertFalse(lab7.is_alternating("842305"))
        self.assertFalse(lab7.is_alternating("285600"))

    def test_my_mod_exp(self):
        a = lab7.my_mod_exp(29, 39, 541)
        self.assertEqual(a, (29 ** 39) % 541)

    def test_last_10_digits(self):
        a = lab7.last_10_digits([2, 3, 4])
        self.assertEqual(a, 4**(3**2))

        a = lab7.last_10_digits([2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(a, 8779806721)


if __name__ == "__main__":
    unittest.main()
