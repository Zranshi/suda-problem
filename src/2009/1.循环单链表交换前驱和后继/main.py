# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 16: 39
# @Author   : Ranshi
# @File     : main.py
# from src.define import ListNode
from pyal.container import ListNode


# START
def change_pre_post(node: ListNode):
    """
    已知node是循环单链表中的一个节点, 要求交换它的前驱和后继.

    先用一个指针循环单链表一遍, 直到指针指向前驱节点. 然后交换节点的前驱和后继.

    Args:
        node (ListNode): 需要更改前驱和后继的节点.
    """
    cur = node
    while cur and cur.next != node:
        cur = cur.next
    if cur and node.next:
        node.next, cur.next = cur, node.next.next


# END
# TEST
if __name__ == "__main__":
    node = ListNode.init_by_lst([1, 3, 4, 1, 2, 4, 56, 7])
