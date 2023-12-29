"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
    输入：l1 = [1,2,4], l2 = [1,3,4]
    输出：[1,1,2,3,4,4]

示例 2：
    输入：l1 = [], l2 = []
    输出：[]

示例 3：
    输入：l1 = [], l2 = [0]
    输出：[0]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.stop = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop:
            raise StopIteration
        current = self.val
        if self.next:
            self.val = self.next.val
            self.next = self.next.next
        else:
            self.stop = True
        return current

    def __eq__(self, other) -> bool:
        if isinstance(other, ListNode):
            while True:
                try:
                    current = next(self)
                    other_current = next(other)
                    if current == other_current:
                        continue
                    return False
                except StopIteration:
                    break
            return True
        return False


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """递归调用"""
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val < list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    list2.next = merge_two_lists(list1, list2.next)
    return list2
