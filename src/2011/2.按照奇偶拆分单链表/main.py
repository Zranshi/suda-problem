# -*- coding:utf-8 -*-
# @Time     : 2021/7/25 11:14
# @Author   : Ranshi
# @File     : main.py
from src.define import ListNode


# START
def split_link(node: ListNode) -> (ListNode, ListNode):
    head, odd, even = ListNode(val=-1, _next=node), ListNode(), ListNode()
    odd_ptr, even_ptr = odd, even
    idx = 0
    while head.next:
        if idx % 2 == 0:
            even_ptr.next, head.next, even_ptr = head.next, head.next.next, head.next
            even_ptr.next = None
        else:
            odd_ptr.next, head.next, odd_ptr = head.next, head.next.next, head.next
            odd_ptr.next = None
        idx += 1
    return even.next, odd.next


# END


# TEST
if __name__ == '__main__':
    ln = ListNode.init_list(list('0123456789'))
    e, o = split_link(ln)
    print(e, o)
