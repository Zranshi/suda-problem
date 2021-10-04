# -*- coding:utf-8 -*-
# @Time     : 2021/7/27 09:49
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define import CSTreeNode


# START
def get_node_number(node: Optional[CSTreeNode]) -> int:
    return (
        1 + get_node_number(node.next_sibling) + get_node_number(node.child)
        if node
        else 0
    )


# END
