# -*- coding:utf-8 -*-
# @Time     : 2021/07/29 17:40
# @Author   : Ranshi
# @File     : main.py
from pyal.container import ListNode


# START
def copy_without_same_node(node: ListNode) -> ListNode:
    new_node = node
    node_map = set()
    while node.next:
        if node.next.val in node_map:
            node.next = node.next.next
        else:
            node_map.add(node.next.val)
            node = node.next
    return new_node


# END
# TEST
if __name__ == "__main__":
    head = ListNode(
        val=0,
        next=ListNode.init_by_lst([1, 23, 1, 1, 1, 3, 3, 4, 1, 4, 5, 6, 7]),
    )
    print(head.next)
    new_head = copy_without_same_node(head)
    print(new_head.next)
