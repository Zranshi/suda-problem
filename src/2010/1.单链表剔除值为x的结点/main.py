# -*- coding:utf-8 -*-
# @Time     : 2021/7/24 10: 32
# @Author   : Ranshi
# @File     : main.py
import sys
from typing import Optional

sys.path.append("/Users/rs/Documents/projects/python_project/suda-problem")
from src.define import ListNode


# START
def remove_x(node: Optional[ListNode], x: int):
    head = ListNode(val=-1, _next=node)
    cur = head
    while cur.next:
        if cur.next.val == x:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head.next


# END

# TEST
if __name__ == '__main__':
    ln = ListNode.init_list([1, 2, 3, 1, 2, 3, 4, 2, 3])
    print(ln)
    print(remove_x(ln, 2))
