import unittest
import remove_element


class TestRemoveElementCase(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(remove_element.my_solution1([3, 2, 2, 3], 3), 2)
        self.assertEqual(remove_element.my_solution1([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)
        self.assertEqual(remove_element.my_solution1([1, 2, 3, 4, 3, 2, 1], 2), 5)

    def test_solution2(self):
        self.assertEqual(remove_element.my_solution2([3, 2, 2, 3], 3), 2)
        self.assertEqual(remove_element.my_solution2([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)
        self.assertEqual(remove_element.my_solution2([1, 2, 3, 4, 3, 2, 1], 2), 5)


if __name__ == '__main__':
    unittest.main()
