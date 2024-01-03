import unittest
import search_insert


class TestSearchInsertCase(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(search_insert.my_solution1([1, 3, 5, 6], 5), 2)
        self.assertEqual(search_insert.my_solution1([1, 3, 5, 6], 2), 1)
        self.assertEqual(search_insert.my_solution1([1, 3, 5, 6], 7), 4)


if __name__ == '__main__':
    unittest.main()
