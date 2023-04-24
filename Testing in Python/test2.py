import unittest
import main

class TestMain(unittest.TestCase):
    def test_adding_5_correctly(self):
        test_param = 10
        result = main.add_5_to_input(test_param)
        self.assertEqual(result, 15)

    def test_break_the_function(self):
        test_param = 'asidfh'
        result = main.add_5_to_input(test_param)
        self.assertTrue(isinstance(result, ValueError))

if __name__ == '__main__':
    unittest.main()

# NOTE: the test function names should start with 'test' to run all the tests
# NOTE: use "python -m unittest" or "py -m unittest" to run all the tests