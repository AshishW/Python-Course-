import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self): # setUp function is sets up before each test
        print('about to test a function')

    def test_adding_5_correctly(self):
        '''
        Hello this is a test
        '''
        test_param = 10
        result = main.add_5_to_input(test_param)
        self.assertEqual(result, 15)

    def test_break_the_function(self):
        test_param = 'asidfh'
        result = main.add_5_to_input(test_param)
        self.assertTrue(isinstance(result, ValueError))
    def tearDown(self):
        # we can use this if we want to clean up some variables or reset some variables
        print('cleaning up')

if __name__ == '__main__':
    unittest.main()

# NOTE: the test function names should start with 'test' to run all the tests
# NOTE: use "python -m unittest" or "py -m unittest" to run all the tests in all test files
# we can also add "-v" for verbos

# NOTE: we can use setUp function which sets up before each test and we can use it if we want to set up default variables or something that we want to test before each test runs

# NOTE: we can use tearDown function to clean up things at the end of each test run