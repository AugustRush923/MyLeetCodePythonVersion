import unittest
import length_of_last_word


class TestLengthOfLastWordCase(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(length_of_last_word.my_solution1("   fly me   to   the moon  "), 4)
        self.assertEqual(length_of_last_word.my_solution1("luffy is still joyboy"), 6)
        self.assertEqual(length_of_last_word.my_solution1("Hello World"), 5)


if __name__ == '__main__':
    unittest.main()
