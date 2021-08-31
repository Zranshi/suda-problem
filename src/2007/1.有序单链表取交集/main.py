# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 11: 41
# @Author   : Ranshi
# @File     : main.py
from src.define import ListNode


# START
def intersection(l1: ListNode, l2: ListNode) -> ListNode:
    """
    求两个有序单链表的交集, 存放在l1中.
    设置两个指针分别指向两个链表的开头, 如果两个指针指向的结点的值相同, 则表示位于交集内.
    如果不相同, 则比较两个结点的值的大小, 如果l1的大, 则移动l2的指针. 否则删除当前l1的结点.

    Args:
        l1 (ListNode): 有序单链表1
        l2 (ListNode): 有序单链表2

    Returns:
        ListNode: 交集的单链表
    """
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
    a = ListNode.init_list([1, 2, 3, 4, 5, 7])
    b = ListNode.init_list([1, 2, 4, 7, 8])
    if a and b:
        print(intersection(a, b))
