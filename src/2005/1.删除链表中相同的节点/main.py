# -*- coding:utf-8 -*-
# @Time     : 2021/7/3 17: 39
# @Author   : Ranshi
# @File     : main.py
from typing import Optional

from src.define import ListNode


# START
def remove_same(node: Optional[ListNode]) -> Optional[ListNode]:
    """
    删除链表中相同的节点.
    创建一个集合, 然后遍历链表, 如果当前值不在集合中, 则将其加入集合, 如果存在, 则跳过当前结点.
    因为需要跳过结点, 因此指针应该位于当前结点的前驱结点, 跳过结点也就是前驱结点的next指向了后继结点.

    Args:
        node (Optional[ListNode]): 待去重的链表

    Returns:
        Optional[ListNode]: 去重后的链表
    """
    if not node:  # 如果为空直接返回
        return node
    point_s, idx = set(), node  # 创建一个集合，用于判定当前结点是否存在过
    while idx.next:
        if idx.next.val in point_s:  # 如果存在，则删除当前结点
            idx.next = idx.next.next
        else:  # 如果不存在，则将其加入到集合中，并移动idx
            point_s.add(idx.next.val)
            idx = idx.next


# ENDs

# TEST
if __name__ == '__main__':
    head = ListNode(val=-1)
    head.push_head(2)
    head.push_head(3)
    head.push_head(4)
    head.push_head(2)
    head.push_head(4)
    print(head)
    remove_same(head)
    print(head)
