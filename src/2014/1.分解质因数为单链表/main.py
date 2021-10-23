# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 09:48
# @Author   : Ranshi
# @File     : main.py
from pyal.container import ListNode


# START
def get_prime_factor(num: int) -> ListNode:
    """
    将一个正整数分解其质因数由到小组成的链表.

    例如对于 2100 可以分解成 7 5 5 3 2 2,
    因此就返回链表: 7->5->5->3->2->2.

    Args:
        num (int): 输入的正整数.

    Returns:
        ListNode: 质因数由大到小组成的链表.
    """
    head = ListNode()
    cur, idx = head, num // 2
    while num > 1 and idx > 1:
        if num % idx == 0:
            for i in range(2, idx // 2 + 1):
                if idx % i == 0:
                    break
            else:
                cur.next = ListNode(idx)
                cur = cur.next
                num //= idx
                idx += 1
        idx -= 1
    return head.next


# END
# TEST
if __name__ == "__main__":
    ln = get_prime_factor(2100)
    print(ln)
