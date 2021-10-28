# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 18:53
# @Author   : Ranshi
# @File     : main.py
from typing import List, Optional

from pyal.container import TreeNode


# START
def init_tree_by_list(
    chs: Optional[List[str]], idx: int = 0
) -> Optional[TreeNode]:
    """
    递归创建二叉树.

    Args:
        chs (Optional[List[str]]): 二叉树堆值的列表.
        idx (int, optional): 当前节点所在列表的下标. Defaults to 0.

    Returns:
        Optional[TreeNode]: 生成的二叉树.
    """
    if chs and idx < len(chs):
        return TreeNode(
            val=chs[idx],
            left=init_tree_by_list(chs, idx * 2 + 1),
            right=init_tree_by_list(chs, idx * 2 + 2),
        )


# END

# TEST
if __name__ == "__main__":
    chs: List[str] = list("swefdsaqwddgcsf")
    node = init_tree_by_list(chs)
    if node:
        print(node)
