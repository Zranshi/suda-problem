# -*- coding:utf-8 -*-
# @Time     : 2021/7/27 09:53
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define.ListNode import ListNode


# START
def remove_item(node: Optional[ListNode], item) -> Optional[ListNode]:
    if node:
        if node.val == item:
            return remove_item(node.next, item)
        node.next = remove_item(node.next, item)
        return node


# END

# TEST
if __name__ == "__main__":
    ln = ListNode.init_list(
        [1, 2, 3, 1, 2, 3, 1, 2, 2, 2, 12, 312, 3, 12, 312, 3, 12]
    )
    print(ln)
    print(remove_item(ln, 2))
