# -*- coding:utf-8 -*-
# @Time     : 2021/7/3 17: 39
# @Author   : Ranshi
# @File     : main.py

class ListNode(object):
    def __init__(self, val: int, _next: 'ListNode' = None):
        self.val = val
        self.next = _next

    def push(self, val: int):
        new_node = ListNode(val=val, _next=self.next)
        self.next = new_node

    def remove_same(self):
        if not self:  # 如果为空直接返回
            return self
        point_s, idx = set(), self  # 创建一个集合，用于判定当前结点是否存在过
        while idx.next:
            if idx.next.val in point_s:  # 如果存在，则删除当前结点
                idx.next = idx.next.next
            else:  # 如果不存在，则将其加入到集合中，并移动idx
                point_s.add(idx.next.val)
                idx = idx.next

    def __str__(self):
        res = []
        idx = self
        while idx.next:
            res.append(str(idx.next.val))
            idx = idx.next
        return ''.join(res)


if __name__ == '__main__':
    head = ListNode(val=-1)
    head.push(2)
    head.push(3)
    head.push(4)
    head.push(2)
    head.push(4)
    print(head)
    head.remove_same()
    print(head)
