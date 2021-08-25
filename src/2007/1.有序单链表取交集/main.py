# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 11: 41
# @Author   : Ranshi
# @File     : main.py
from src.define import ListNode


# START
def intersection(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2:
        return l1
    h1, h2 = ListNode(0, l1), ListNode(0, l2)
    t1, t2 = h1, h2
    while t1.next and t2.next:
        # 如果相等则t1,t2移动到下一格
        if t1.next.val == t2.next.val:
            t1, t2 = t1.next, t2.next
        # 如果大于则移动t2, 直到相等或者大于t1.val
        elif t1.next.val > t2.next.val:
            t2 = t2.next
        # 如果t1.val < t2.val 则移动t1, 且跳过当前结点
        else:
            t1.next = t1.next.next
    return l1


# END

# TEST
if __name__ == '__main__':
    a, b = ListNode(), ListNode()
    a.push_head(7)
    a.push_head(5)
    a.push_head(5)
    a.push_head(4)
    a.push_head(3)
    a.push_head(2)
    a.push_head(1)
    b.push_head(8)
    b.push_head(7)
    b.push_head(4)
    b.push_head(4)
    b.push_head(4)
    b.push_head(2)
    b.push_head(1)
    print(intersection(a, b))
