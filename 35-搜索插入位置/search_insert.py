"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。请必须使用时间复杂度为 O(log n) 的算法。

示例 1:
    输入: nums = [1,3,5,6], target = 5
    输出: 2

示例 2:
    输入: nums = [1,3,5,6], target = 2
    输出: 1

示例 3:
    输入: nums = [1,3,5,6], target = 7
    输出: 4
"""

from typing import List


def my_solution1(nums: List[int], target: int) -> int:
    """暴力匹配"""
    for index, num in enumerate(nums):
        # 如果当前与目标匹配则返回当前下标 or 如果当前大于目标则返回当前下标
        if num == target or num > target:
            return index
        # 如果当前小于目标则继续下一次循环
        if num < target:
            # 当循环到最后时，代表数组中没有目标值
            if index == len(nums) - 1:
                return len(nums)
            continue
