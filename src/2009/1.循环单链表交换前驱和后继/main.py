# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 16: 39
# @Author   : Ranshi
# @File     : main.py

from src.define import ListNode


# START
def change_pre_post(node: ListNode):
    cur = node
    while cur.next == node:
        cur = cur.next
    node.next, cur.next = cur, node.next.next

# END

