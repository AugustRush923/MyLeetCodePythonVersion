import unittest
import two_sum


class TestSolution1(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(two_sum.my_first_solution([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum.my_first_solution([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum.my_first_solution([3, 3], 6), [0, 1])

    def test_solution2(self):
        self.assertEqual(two_sum.my_second_solution([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum.my_second_solution([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum.my_second_solution([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()
