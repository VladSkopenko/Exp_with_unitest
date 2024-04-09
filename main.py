import unittest


def multiply_numbers(x, y):
    """
    The multiply_numbers function multiplies two numbers together and returns the result.

    :param x: Multiply the y parameter
    :param y: Multiply the x parameter
    :return: The product of x and y
    :doc-author: Trelent
    """
    return x * y


class TestMultiplication(unittest.TestCase):
    def test_multiply_two_positive_numbers(self):
        """
        The test_multiply_two_positive_numbers function tests the multiply_numbers function with two positive numbers.
        The expected result is 6.

        :param self: Access the class attributes and methods
        :return: The result of the multiply_numbers function
        :doc-author: Trelent
        """
        result = multiply_numbers(2, 3)
        self.assertEqual(result, 6)

    def test_multiply_positive_and_negative_numbers(self):
        """
        The test_multiply_positive_and_negative_numbers function tests the multiply_numbers function with two arguments, 2 and -3.
        The expected result is -6.

        :param self: Access the class methods and attributes
        :return: -6
        :doc-author: Trelent
        """
        result = multiply_numbers(2, -3)
        self.assertEqual(result, -6)

    def test_multiply_two_negative_numbers(self):
        """
        The test_multiply_two_negative_numbers function tests the multiply_numbers function with two negative numbers.
        The expected result is 6.

        :param self: Access the class attributes and methods
        :return: 6
        :doc-author: Trelent
        """
        result = multiply_numbers(-2, -3)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
