# -*- coding:utf-8 -*-
# @Time     : 2021/7/25 11:14
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from pyal.container import ListNode


# START
def split_linked_list(node: Optional[ListNode]) -> tuple[ListNode, ListNode]:
    """
    将单链表拆分为全为奇数和全为偶数的两个单链表.

    Args:
        node (Optional[ListNode]): 单链表.

    Returns:
        tuple[ListNode, ListNode]: 全为奇数的单链表和全为偶数的单链表
    """
    even_list, head = ListNode(), ListNode(val=0, next=node)
    cur = head
    while cur and cur.next:
        if cur.next.val % 2 == 0:
            tmp, cur.next = cur.next, cur.next.next
            even_list.next, tmp.next = tmp, even_list.next
        cur = cur.next
    return head.next, even_list.next


# END

# TEST
if __name__ == "__main__":
    ln = ListNode.init_by_lst([1, 2, 3, 4, 5, 6, 7, 8, 9])
    e, o = split_linked_list(ln)
    print(e, o)
