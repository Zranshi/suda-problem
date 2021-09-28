# -*- coding:utf-8 -*-
# @Time     : 2021/07/31 23:02
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define.Tree import SearchTree


# START
def max_k(node: Optional[SearchTree], k: int) -> Optional[SearchTree]:
    if not node:
        return None
    if node.r_size == k - 1:
        return node
    elif node.r_size < k - 1:
        return max_k(node.left, k - 1 - node.r_size)
    else:
        return max_k(node.right, k)


# END
