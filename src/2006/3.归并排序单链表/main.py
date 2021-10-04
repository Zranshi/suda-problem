# -*- coding:utf-8 -*-
# @Time     : 2021/7/19 09: 48
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define import ListNode


# START
def merge_sort_ln(head: ListNode) -> Optional[ListNode]:
    """
    归并排序算法排序单链表.

    Args:
        head (ListNode): 单链表的头结点.

    Returns:
        Optional[ListNode]: 排序后的单链表头结点.
    """

    def merge_ln(
        h1: Optional[ListNode], h2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        合并函数. 将两个排序好的单链表合并为一个排序好的单链表.

        Args:
            h1 (Optional[ListNode]): 第一个排序好的单链表.
            h2 (Optional[ListNode]): 第二个排序好的单链表.

        Returns:
            Optional[ListNode]: 合并完成的单链表.
        """
        d_h = ListNode()
        t, t1, t2 = d_h, h1, h2
        while t1 and t2:
            if t1.val <= t2.val:
                t.next, t1 = t1, t1.next
            else:
                t.next, t2 = t2, t2.next
            t = t.next
        t.next = t1 or t2
        if not d_h.next:
            return None
        return d_h.next

    def sort_func(
        h: Optional[ListNode], tail: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        """
        递归拆分函数. 拆分直到头结点和尾结点中间仅剩一个结点, 或者没有结点.
        采用快慢指针的方式找到头尾结点的中间结点, 然后拆分为两部分.

        Args:
            h (Optional[ListNode]): 拆分的头结点
            tail (Optional[ListNode], optional): 拆分的尾结点. Defaults to None.

        Returns:
            Optional[ListNode]: 返回排序好的单链表.
        """
        if not h:
            return h
        if h.next == tail:
            h.next = None
            return h
        slow = fast = h
        while slow and fast and fast != tail:
            slow, fast = slow.next, fast.next
            if fast != tail and fast:
                fast = fast.next
        mid = slow
        return merge_ln(sort_func(h, mid), sort_func(mid, tail))

    return sort_func(head)


# END

# TEST
if __name__ == "__main__":
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
    print(f"before sort: {h}")
    merge_sort_ln(h)
    print(f"after sort : {h}")
