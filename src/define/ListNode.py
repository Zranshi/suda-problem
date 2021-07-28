# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 11: 51
# @Author   : Ranshi
# @File     : ListNode.py
from typing import Any, List, Optional


class LinkList:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def push_tail(self, val: int):
        node = ListNode(val=val)
        self.tail.next, self.tail = node, node

    def __str__(self):
        cur, res = self.head.next, []
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return '->'.join(res)


class ListNode:
    def __init__(self, val: int = 0, _next: Optional['ListNode'] = None):
        self.val = val
        self.next = _next

    def push_head(self, val: int = 0):
        node = ListNode(val=val, _next=self.next)
        self.next = node

    def __str__(self) -> str:
        res, cur = [], self
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return '->'.join(res)

    @classmethod
    def init_list(cls, arr: List[Any]):
        head = ListNode()
        cur = head
        for x in arr:
            node = ListNode(val=x, _next=None)
            cur.next, cur = node, node
        return head.next
