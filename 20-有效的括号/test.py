import unittest
import is_valid


class TestIsValid(unittest.TestCase):
    def test_my_solution1(self):
        self.assertEqual(is_valid.my_solution1('()'), True)
        self.assertEqual(is_valid.my_solution1('()[]{}'), True)
        self.assertEqual(is_valid.my_solution1('(]'), False)
        self.assertEqual(is_valid.my_solution1('({})'), True)
        self.assertEqual(is_valid.my_solution1('({)(})'), False)
        self.assertEqual(is_valid.my_solution1('(){[]}'), True)


if __name__ == '__main__':
    unittest.main()
