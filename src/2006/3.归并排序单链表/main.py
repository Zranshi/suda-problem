# -*- coding:utf-8 -*-
# @Time     : 2021/7/19 09: 48
# @Author   : Ranshi
# @File     : main.py

# DEFINE
class ListNode:
    def __init__(self, val: int = 0, _next: 'ListNode' = None):
        self.val = val
        self.next = _next

    def push_head(self, val: int = 0):
        node = ListNode(val=val, _next=self.next)
        self.next = node

    def __str__(self):
        res, cur = [], self
        while cur.next:
            res.append(str(cur.next.val))
            cur = cur.next
        return '->'.join(res)


# START
def merge_sort_ln(head: ListNode) -> ListNode:
    def merge_ln(h1: ListNode, h2: ListNode) -> ListNode:
        d_h = ListNode()
        t, t1, t2 = d_h, h1, h2
        while t1 and t2:
            if t1.val <= t2.val:
                t.next, t1 = t1, t1.next
            else:
                t.next, t2 = t2, t2.next
            t = t.next
        if t1:
            t.next = t1
        else:
            t.next = t2
        return d_h.next

    def sort_func(h: ListNode, tail: ListNode = None) -> ListNode:
        if not h:
            return h
        if h.next == tail:
            h.next = None
            return h
        slow = fast = h
        while fast != tail:
            slow, fast = slow.next, fast.next
            if fast != tail and fast:
                fast = fast.next
        mid = slow
        return merge_ln(sort_func(h, mid), sort_func(mid, tail))

    return sort_func(head)


# END

# TEST
if __name__ == '__main__':
    h = ListNode(0)
    h.push_head(2)
    h.push_head(4)
    h.push_head(5)
    h.push_head(6)
    h.push_head(2)
    h.push_head(4)
    h.push_head(6)
    h.push_head(8)
    h.push_head(9)
    h.push_head(3)
    h.push_head(1)
    h.push_head(2)
    print(f'before sort: {h}')
    merge_sort_ln(h)
    print(f'after sort : {h}')
