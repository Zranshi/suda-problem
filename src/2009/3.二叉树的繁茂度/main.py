# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 16: 54
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define import TreeNode


# START
def get_depth(t: Optional[TreeNode]) -> int:
    if not t:
        return 0
    if not t.left and not t.right:
        return 1
    else:
        return max(
            0 if not t.left else 1 + get_depth(t.left),
            0 if not t.right else 1 + get_depth(t.right),
        )


def get_max_width(t: Optional[TreeNode]) -> int:
    from collections import deque

    dq = deque()
    dq.appendleft(t)
    level_num, res, next_level = 1, 0, 0
    while dq:
        idx = dq.pop()
        if idx.left:
            dq.appendleft(idx.left)
            next_level += 1
        if idx.right:
            dq.appendleft(idx.right)
            next_level += 1
        level_num -= 1
        if level_num == 0:
            res = max(res, next_level)
            level_num, next_level = next_level, 0
    return res


def get_luxuriant(t: Optional[TreeNode]) -> int:
    return get_depth(t) * get_max_width(t)


# END

# TEST
if __name__ == "__main__":
    tn = TreeNode.init_by_list(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, 10, 11, 12]
    )
    print(get_luxuriant(tn))
