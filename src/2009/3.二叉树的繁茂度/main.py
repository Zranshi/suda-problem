# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 16: 54
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

# from src.define import TreeNode
from pyal.container import TreeNode


# START
def get_depth(root: Optional[TreeNode]) -> int:
    """
    由顶到下的递归操作, 每次取左子树和右子树中高度较大的一颗子树, 就能得到树的深度.

    Args:
        root (Optional[TreeNode]): 树

    Returns:
        int: 树的深度.
    """
    return (
        max(
            get_depth(root.left) + 1 if root.left else 1,
            get_depth(root.right) + 1 if root.right else 1,
        )
        if root
        else 0
    )


def get_width(t: Optional[TreeNode]) -> int:
    """
    遍历每一层, res取所有层宽度的最大值, 就能找到树的宽度.

    Args:
        t (Optional[TreeNode]): 树

    Returns:
        int: 树的宽度.
    """
    if not t:
        return 0
    lst = [t]
    res = 0
    while lst:
        new_lst = []
        res = max(res, len(lst))
        for node in lst:
            if node.left:
                new_lst.append(node.left)
            if node.right:
                new_lst.append(node.right)
        lst = new_lst
    return res


def get_luxuriant(t: Optional[TreeNode]) -> int:
    return get_depth(t) * get_width(t)


# END

# TEST
if __name__ == "__main__":
    tn = TreeNode.init_by_lst(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, 10, 11, 12]
    )
    print(get_luxuriant(tn))
