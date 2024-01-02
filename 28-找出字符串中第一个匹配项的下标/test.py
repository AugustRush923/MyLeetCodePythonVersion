import unittest
import str_str


class TestStrStrCase(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(str_str.my_solution1("sadbutsad", "sad"), 0)
        self.assertEqual(str_str.my_solution1("leetcode", "leeto"), -1)
        self.assertEqual(str_str.my_solution1("mississippi", "issi"), 1)
        self.assertEqual(str_str.my_solution1("abc", "c"), 2)


if __name__ == '__main__':
    unittest.main()
