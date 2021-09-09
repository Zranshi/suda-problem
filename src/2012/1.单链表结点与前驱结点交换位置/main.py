# -*- coding:utf-8 -*-
# @Time     : 2021/7/26 13:04
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define import ListNode


# START
def change(node: Optional[ListNode], i: int) -> Optional[ListNode]:
    idx = 1
    head = ListNode(val=0, _next=node)
    cur = head
    while cur.next:
        if idx == i:
            node1 = cur.next
            node2 = cur.next.next
            cur.next = node2
            if node2:
                node1.next = node2.next
                node2.next = node1
            break
        idx += 1
        cur = cur.next
    return head.next


# END

# TEST
if __name__ == "__main__":
    ln = ListNode.init_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(ln)
    print(change(ln, 3))
