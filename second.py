import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        """
        The setUp function is run before each test function.
        It creates a list of integers that will be used in the tests.

        :param self: Represent the instance of the object that is calling this method
        :return: The list [ 1, 2, 3 ]
        :doc-author: Trelent
        """
        self.my_list = [1, 2, 3]

    def tearDown(self):
        """
        The tearDown function is called after each test function.
        It is used to clean up the objects created in setUp.

        :param self: Make the function belong to the class
        :return: Nothing
        :doc-author: Trelent
        """
        del self.my_list

    def test_list_length(self):
        """
        The test_list_length function tests the length of the list.
        It asserts that the length of my_list is equal to 3.

        :param self: Access the instance attributes and methods
        :return: The length of the list
        :doc-author: Trelent
        """
        self.assertEqual(len(self.my_list), 3)

    def test_list_contents(self):
        """
        The test_list_contents function tests that the contents of my_list are equal to [ 1, 2, 3 ].


        :param self: Refer to the instance of the class
        :return: A list of numbers
        :doc-author: Trelent
        """
        self.assertListEqual(self.my_list, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
