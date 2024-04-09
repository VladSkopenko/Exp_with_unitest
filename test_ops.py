import unittest

from ops import add
from ops import div
from ops import mul
from ops import sub


class TestExamples(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        The setUpClass function is called once for the class.
        It is used to perform setup that should be done before any of the tests are run.

        :param cls: Pass the class object to the function
        :return: A class object
        :doc-author: Trelent
        """
        print("Start before all test")

    @classmethod
    def tearDownClass(cls):
        """
        The tearDownClass function is called after all tests in the class have been run.
        It is used to clean up any resources that were created during the setUpClass function.

        :param cls: Reference the class that is being tested
        :return: The test result
        :doc-author: Trelent
        """
        print("Start after all test")

    def setUp(self):
        """
        The setUp function is run before each test.
        It creates a new instance of the class, which will be used for testing.

        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        print("Start before each test")

    def tearDown(self):
        """
        The tearDown function is run after each test.
        It's a good place to clean up any resources that were used during the tests, such as closing files or database connections.

        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        print("Start after each test")

    def test_add(self):
        """
        The test_add function tests the add function from the my_calculator library.
            It does this by calling add with arguments 2 and 3, and comparing the result to 5.

        :param self: Represent the instance of the class
        :return: The value of the add function with 2 and 3 as arguments
        :doc-author: Trelent
        """
        print("Add function test")
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        """
        The test_sub function tests the sub function in the calculator.py file.
        It does this by using a unit test from unittest, which is imported at the top of this file.
        The assertEquals method compares two values and returns an error if they are not equal.

        :param self: Represent the instance of the class
        :return: - 1
        :doc-author: Trelent
        """
        print("Sub function test")
        self.assertEqual(sub(2, 3), -1)

    def test_mul(self):
        """
        The test_mul function tests the mul function from the my_calculator library.
            It does this by calling the mul function with two arguments, 2 and 3, and
            comparing its output to 6.

        :param self: Represent the instance of the class
        :return: The result of the mul function, which is 6
        :doc-author: Trelent
        """
        print("Mul function test")
        self.assertEqual(mul(2, 3), 6)

    def test_div(self):
        """
        The test_div function tests the div function in the calculator.py file.
        It uses assertAlmostEquals to test if 2/3 is equal to 0.66666666, and it uses
        assertRaises as a context manager to check if ZeroDivisionError is raised when 3/0
        is attempted.

        :param self: Access the instance of the class
        :return: The result of the div function
        :doc-author: Trelent
        """
        print("Div function test")
        self.assertAlmostEqual(div(2, 3), 0.66666666)
        with self.assertRaises(ZeroDivisionError) as cm:
            div(3, 0)


if __name__ == "__main__":
    unittest.main()
