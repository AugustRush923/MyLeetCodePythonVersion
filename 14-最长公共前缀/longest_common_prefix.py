"""
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 ""。

示例 1：
    输入：strs = ["flower","flow","flight"]
    输出："fl"

示例 2：
    输入：strs = ["dog","racecar","car"]
    输出：""
    解释：输入不存在公共前缀。
"""
from typing import List


def my_solution1(strs: List[str]) -> str:
    min_length = min([len(s) for s in strs])
    common_prefix = ""
    for i in range(min_length):
        common_prefix += strs[0][i]
        for s in strs[1:]:
            if s[:i + 1] == common_prefix:
                continue
            common_prefix = common_prefix[:i]
            return common_prefix
    return common_prefix
