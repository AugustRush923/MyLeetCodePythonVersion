import unittest
import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(is_palindrome.my_solution(121), True)
        self.assertEqual(is_palindrome.my_solution(-121), False)
        self.assertEqual(is_palindrome.my_solution(10), False)
        self.assertEqual(is_palindrome.my_solution(1001), True)


if __name__ == '__main__':
    unittest.main()
