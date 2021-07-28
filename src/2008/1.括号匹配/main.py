# -*- coding:utf-8 -*-
# @Time     : 2021/7/22 10: 27
# @Author   : Ranshi
# @File     : main.py


# START
def bracket_matching(string: str):
    res, stack = [], []
    start = {'(': 1, '[': 2, '{': 3}
    end = {')': 1, ']': 2, '}': 3}
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
if __name__ == '__main__':
    s = '{{()[()](){}}}'
    print(bracket_matching(s))
