# -*- coding:utf-8 -*-
# @Time     : 2021/7/3 17: 39
# @Author   : Ranshi
# @File     : main.py
import sys
from typing import Optional

sys.path.append("/Users/rs/Documents/projects/python_project/suda-problem")
from src.define import ListNode


# START
def remove_same(node: ListNode) -> Optional[ListNode]:
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
