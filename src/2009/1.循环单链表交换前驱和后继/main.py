# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 16: 39
# @Author   : Ranshi
# @File     : main.py
from src.define.ListNode import ListNode


# START
def change_pre_post(node: ListNode):
    cur = node
    while cur and cur.next == node:
        cur = cur.next
    if cur and node.next:
        node.next, cur.next = cur, node.next.next


# END
