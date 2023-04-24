import unittest
from unittest import result
import guessing_game2


class TestGame(unittest.TestCase):
    def test_guess(self):
        test_guess = 10
        result = guessing_game2.guessed_correctly(test_guess, 10)
        self.assertTrue(result)

    def test_wrong_guess(self):
        test_guess = 4
        result = guessing_game2.guessed_correctly(test_guess, 10)
        self.assertFalse(result)

    def test_wrong_number(self):
        result = guessing_game2.guessed_correctly(12, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = guessing_game2.guessed_correctly('asdf', 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
