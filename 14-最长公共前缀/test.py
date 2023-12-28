import unittest
import longest_common_prefix


class MyLongestCommonPrefix(unittest.TestCase):
    def test_my_solution1(self):
        self.assertEqual(longest_common_prefix.my_solution1(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix.my_solution1(["dog", "racecar", "car"]), "")


if __name__ == '__main__':
    unittest.main()
