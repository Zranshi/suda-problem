# -*- coding:utf-8 -*-
# @Time     : 2021/7/26 13:04
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from pyal.container import ListNode


# START
def change(node: Optional[ListNode], i: int) -> Optional[ListNode]:
    """
    将单链表中编号为 i (从 0 开始)的节点和它的前驱节点交换位置.

    因为为单链表, 所以需要在cur.next.next为目标节点时, 才能操作如何指向前驱节点.

    Args:
        node (Optional[ListNode]): 单链表.
        i (int): 目标节点编号.

    Returns:
        Optional[ListNode]: 交换后的链表.
    """
    idx = 1
    head = ListNode(val=0, next=node)
    cur = head
    while cur.next:
        if idx == i:
            target = cur.next.next
            cur.next.next, cur.next, target.next = target.next, target, cur.next
            break
        idx += 1
        cur = cur.next
    return head.next


# END

# TEST
if __name__ == "__main__":
    print(change(node=ListNode.init_by_lst([0, 1, 2, 3]), i=3))
