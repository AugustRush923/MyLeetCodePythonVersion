"""
给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
示例1：
输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
解释：因为
nums[0] + nums[1] == 9 ，返回[0, 1] 。

示例2：
输入：nums = [3, 2, 4], target = 6
输出：[1, 2]

示例3：
输入：nums = [3, 3], target = 6
输出：[0, 1]
"""


def my_first_solution(nums: list, target: int) -> list:
    """通过双循环解决"""
    result = []
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            # 如果与结果相等则添加到结果列表中
            if nums[i] + nums[j] == target:
                result.extend([i, j])
    return result


def my_second_solution(nums: list, target: int) -> list:
    """通过HashMap解决"""
    hashmap = {}
    for index, num in enumerate(nums):
        # 首先在HashMap中查找与结果匹配的键
        if hashmap.get(target - num) is not None:
            return [hashmap.get(target - num), index]
        # 如果没有匹配则先将此键插入HashMap中
        hashmap[num] = index
    return []
