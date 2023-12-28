"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。

示例 1：
    输入：s = "()"
    输出：true

示例 2：
    输入：s = "()[]{}"
    输出：true

示例 3：
    输入：s = "(]"
    输出：false
"""


def my_solution1(s: str) -> bool:
    # 定义一个栈
    stack = []
    # 定义一个映射关系
    mapping = {')': '(', ']': '[', '}': '{'}

    for c in s:
        # 左半部分直接压进栈中
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        else:
            # 如果右半部分和栈中最新的无法匹配 或 栈中无值时就不是合法的
            if mapping[c] != stack[len(stack) - 1] or len(stack) == 0:
                return False
            # 匹配上则把最新的从栈中弹出
            stack.pop()

    return len(stack) == 0
