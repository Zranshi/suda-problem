# -*- coding:utf-8 -*-
# @Time     : 2021/7/27 09:49
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from pyal.container import CSTree


# START
def get_node_number(node: Optional[CSTree]) -> int:
    """
    返回节点数量.

    当前节点的子树的节点数量 = 1 + 所有孩子的节点子树的节点数量.

    Args:
        node (Optional[CSTree]): 孩子兄弟法表示的树结构.

    Returns:
        int: 节点总数.
    """
    return (
        1 + get_node_number(node.next_sibling) + get_node_number(node.child)
        if node
        else 0
    )


# END
