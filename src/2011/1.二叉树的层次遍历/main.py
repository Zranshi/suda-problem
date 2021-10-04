# -*- coding:utf-8 -*-
# @Time     : 2021/7/25 10:49
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define import TreeNode


# START
def level_order(node: Optional[TreeNode]) -> list:
    from collections import deque

    dq, res = deque(), []
    dq.appendleft(node)
    while dq:
        idx = dq.pop()
        res.append(idx.val)
        if idx.left:
            dq.appendleft(idx.left)
        if idx.right:
            dq.appendleft(idx.right)
    return res


# END

# TEST
if __name__ == "__main__":
    tree = TreeNode.init_by_list(
        [item if item != " " else "" for item in "123456 7 89"]
    )
    print(level_order(tree))
