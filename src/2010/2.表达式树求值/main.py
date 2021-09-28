# -*- coding:utf-8 -*-
# @Time     : 2021/7/24 10: 52
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define.Tree import TreeNode


# START
def calculate(t: Optional[TreeNode]) -> int:
    if not t:
        return -1

    if not t.left and not t.right:
        return t.val
    return eval(f"{calculate(t.left)}{t.val}{calculate(t.right)}")


# END

# TEST
if __name__ == "__main__":
    et = TreeNode.init_by_list(
        [item if item != " " else "" for item in "+-*15-7    89  "]
    )
    print(calculate(et))
