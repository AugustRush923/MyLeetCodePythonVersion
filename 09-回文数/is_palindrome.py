"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。

示例 1：
    输入：x = 121
    输出：true

示例 2：
    输入：x = -121
    输出：false
    解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
    输入：x = 10
    输出：false
    解释：从右向左读, 为 01 。因此它不是一个回文数。
"""


def my_solution(x: int) -> bool:
    # 如果小于0一定不是回文数
    if x < 0:
        return False
    # 将数字转化为string
    str_x = str(x)
    # 倒叙生成新string
    reverse_x = ''.join([str_x[len(str_x)-1-i] for i, x in enumerate(str_x)])
    # 对比两个string是否相等
    if str(x) == reverse_x:
        return True
    return False
