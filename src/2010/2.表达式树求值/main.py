# -*- coding:utf-8 -*-
# @Time     : 2021/7/24 10: 52
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

# from src.define import TreeNode
from pyal.container import TreeNode


# START
def calculate(t: Optional[TreeNode]) -> int:
    """
    求解计算树的值.

    Args:
        t (Optional[TreeNode]): 计算树, 叶子节点为数值, 节点为运算符.

    Returns:
        int: 求解的值.
    """
    if not t:
        return -1

    if not t.left and not t.right:
        return t.val
    return eval(f"{calculate(t.left)}{t.val}{calculate(t.right)}")


# END

# TEST
if __name__ == "__main__":
    et = TreeNode.init_by_lst(
        [item if item != " " else "" for item in "+-*15-7    89  "]
    )
    print(calculate(et))
