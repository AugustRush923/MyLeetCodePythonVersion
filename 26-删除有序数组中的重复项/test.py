import unittest
import remove_duplicates


class MyTestCase(unittest.TestCase):
    @staticmethod
    def verify_function(nums, expected_nums, func):
        length = func(nums)
        if not length == len(expected_nums):
            return False
        for i in range(len(expected_nums)):
            if not nums[i] == expected_nums[i]:
                return False
        return True

    def test_solution1(self):
        self.assertEqual(self.verify_function([1, 1, 2], [1, 2], remove_duplicates.my_solution1), True)
        self.assertEqual(self.verify_function([-1, 0, 0, 0, 0, 3, 3], [-1, 0, 3], remove_duplicates.my_solution1), True)
        self.assertEqual(
            self.verify_function([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], remove_duplicates.my_solution1), True)

    def test_solution2(self):
        self.assertEqual(self.verify_function([1, 1, 2], [1, 2], remove_duplicates.solution2), True)
        self.assertEqual(self.verify_function([-1, 0, 0, 0, 0, 3, 3], [-1, 0, 3], remove_duplicates.solution2), True)
        self.assertEqual(
            self.verify_function([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], remove_duplicates.solution2), True)


if __name__ == '__main__':
    unittest.main()
