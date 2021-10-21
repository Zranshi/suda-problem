# -*- coding:utf-8 -*-
# @Time     : 2021/7/24 10: 32
# @Author   : Ranshi
# @File     : main.py
from typing import Optional
from pyal.container import ListNode

# START
def remove_x(node: Optional[ListNode], target: int):
    """
    删除所有节点值为target的节点, 需要注意应该判断cur.next的值.

    Args:
        node (Optional[ListNode]): 单链表
        target (int): 目标值

    Returns:
        [type]: 删除后的单链表
    """
    head = ListNode(val=-1, next=node)
    cur = head
    while cur.next:
        if cur.next.val == target:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head.next


# END

# TEST
if __name__ == "__main__":
    ln = ListNode.init_by_list([1, 2, 3, 1, 2, 3, 4, 2, 3])
    print(ln)
    print(remove_x(ln, 2))
