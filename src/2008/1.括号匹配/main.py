# -*- coding:utf-8 -*-
# @Time     : 2021/7/22 10: 27
# @Author   : Ranshi
# @File     : main.py
from typing import List, Tuple

# START


def bracket_matching(string: str) -> List[Tuple[int, int]]:
    """
    括号匹配, 给一个包含多种括号的字符串, 返回各个括号及其反括号的下标.

    使用栈匹配括号. 具体算法如下:
    - 如果当前字符是括号, 则压入栈.
    - 如果是反括号, 则判断其和栈顶的括号是否匹配. 如果匹配则记录两者的下标, 并推出栈顶的括号
      如果不匹配, 说明字符串是非法的括号字符串.

    Args:
        string (str): 一个包含多种括号的字符串.

    Returns:
        List[Tuple[int, int]]: 返回匹配括号的下标数组
    """
    res, stack = [], []
    start = {"(": 1, "[": 2, "{": 3}
    end = {")": 1, "]": 2, "}": 3}
    for i, ch in enumerate(string):
        if ch in start:
            stack.append((ch, i))
        if ch in end:
            if end[ch] != start[stack[-1][0]]:
                return None
            else:
                res.append((stack[-1][1], i))
                stack.pop()
    return res if not stack else None


# END

# TEST
if __name__ == "__main__":
    s = "{{()[()](){}}}"
    print(bracket_matching(s))
