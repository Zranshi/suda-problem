# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 20:29
# @Author   : Ranshi
# @File     : main.py
from typing import Set

from pyal.container import DulLinkedList


# START
def two_sum1(node: DulLinkedList, target: int) -> str:
    # set实现
    num_set: Set[int] = set()
    cur = node
    while cur:
        if cur.val in num_set:
            return f"{target} = {target - cur.val} + {cur.val}"
        else:
            num_set.add(target - cur.val)
        cur = cur.next
    return "not exist two numbers sum equals target."


def two_sum2(node: DulLinkedList, target: int) -> str:
    """
    两数之和, 双链表版.

    由于采用双链表, 并且有序, 因此可以使用双指针法.

    Args:
        node (DulLinkedList): 双链表.
        target (int): 目标数.

    Returns:
        str: 返回信息.
    """
    cur = node
    while cur.next:
        cur = cur.next
    tail, head = cur, node
    while tail and head and tail != head:
        if tail.val + head.val == target:
            return f"{target} = {head.val} + {tail.val}"
        elif tail.val + head.val < target:
            head = head.next
        else:
            tail = tail.pre
    return "not exist two numbers sum equals target."


# END

# TEST
if __name__ == "__main__":
    dll = DulLinkedList.init_by_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    if dll:
        print(two_sum2(dll, 16))
