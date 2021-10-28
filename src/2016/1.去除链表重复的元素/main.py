# -*- coding:utf-8 -*-
# @Time     : 2021/07/29 17:40
# @Author   : Ranshi
# @File     : main.py
from pyal.container import ListNode


# START
def copy_without_same_node(node: ListNode) -> ListNode:
    """
    去除链表的重复结点.

    采用set去重.

    Args:
        node (ListNode): 链表.

    Returns:
        ListNode: 去重后的链表.
    """
    new_node = node
    node_map = {node.val}
    while node.next:
        if node.next.val in node_map:
            node.next = node.next.next
        else:
            node_map.add(node.next.val)
            node = node.next
    return new_node


# END
# TEST
if __name__ == "__main__":
    ln = ListNode.init_by_lst([1, 23, 1, 1, 1, 3, 3, 4, 1, 4, 5, 6, 7])
    print(ln)
    new_ln = copy_without_same_node(ln)
    print(new_ln)
