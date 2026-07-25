import unittest

from Lotto import calculate_prize

class TestPrize(unittest.TestCase):
    def test_three_win(self):
        player = [1, 2, 3, 4, 5, 6]
        winning = [1, 2, 3, 14, 15, 16]
        result = calculate_prize(player, winning)
        self.assertEqual(result, 170)

    def test_none_win(self):
        player = [1, 2, 3, 4, 5, 6]
        winning = [11, 12, 13, 14, 15, 16]
        result = calculate_prize(player, winning)
        self.assertEqual(result, 0)

    def test_all_win(self):
        player = [1, 2, 3, 4, 5, 6]
        winning = [1, 2, 3, 4, 5, 6]
        result = calculate_prize(player, winning)
        self.assertEqual(result, 20000)


if __name__ == '__main__':
    unittest.main()