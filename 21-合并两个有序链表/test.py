import unittest
import merge_two_lists


class TestSolution(unittest.TestCase):
    def test_solution1(self):
        listNode = merge_two_lists.ListNode
        l1 = listNode(1, listNode(2, listNode(3)))
        l2 = listNode(1, listNode(3, listNode(4)))
        result = listNode(1, listNode(1, listNode(2, listNode(3, listNode(3, listNode(4))))))
        self.assertEqual(result == merge_two_lists.merge_two_lists(l1, l2), True)


if __name__ == '__main__':
    unittest.main()
