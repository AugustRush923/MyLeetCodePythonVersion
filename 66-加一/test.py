import unittest
import plus_one


class TestPlusOneCase(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(plus_one.my_solution1([1, 2, 3]), [1, 2, 4])
        self.assertEqual(plus_one.my_solution1([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(plus_one.my_solution1([0]), [1])


if __name__ == '__main__':
    unittest.main()
