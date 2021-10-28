# -*- coding:utf-8 -*-
# @Time     : 2021/07/31 23:02
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define import SearchTree


# START
def max_k(node: Optional[SearchTree], k: int) -> Optional[SearchTree]:
    """
    求一个二叉排序树中第K大的元素. 每个结点有一个特殊的属性r_size, r_size = 右子树的结点
    个数 + 1.

    可以根据 r_size 求解. 对于每个节点, 可以求得右子树中比它本身大的个数, 那么就可以根据
    二叉排序树的性质进行递归求解了.

    Args:
        node (Optional[SearchTree]): 二叉排序树根结点.
        k (int): 第K大的数.

    Returns:
        Optional[SearchTree]: 返回第K大的结点.
    """
    if not node:
        return None
    if node.r_size == k:
        return node
    elif node.r_size < k:
        return max_k(node.left, k - node.r_size)
    else:
        return max_k(node.right, k)


# END
