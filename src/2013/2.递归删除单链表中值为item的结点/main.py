# -*- coding:utf-8 -*-
# @Time     : 2021/7/27 09:53
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from pyal.container import ListNode


# START
def remove_item(node: Optional[ListNode], target) -> Optional[ListNode]:
    """
    递归删除单链表中值为target的节点.

    如果当前节点的值为target则丢弃当前节点, 返回处理完之后节点的单链表.
    如果当前节点的值不会target, 则处理完之后的节点, 并修改当前节点的next指针, 最后返回当前节点.

    Args:
        node (Optional[ListNode]): 当前节点.
        target ([type]): 要删除的目标值.

    Returns:
        Optional[ListNode]: 删除所有值为target的节点的单链表.
    """
    if node:
        if node.val == target:
            return remove_item(node.next, target)
        node.next = remove_item(node.next, target)
        return node


# END

# TEST
if __name__ == "__main__":
    ln = ListNode.init_by_lst(
        [1, 2, 3, 1, 2, 3, 1, 2, 2, 2, 12, 312, 3, 12, 312, 3, 12]
    )
    print(ln)
    print(remove_item(ln, 2))
