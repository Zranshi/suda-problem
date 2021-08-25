# coding: utf-8
# @Time     : 2021/08/11 17:45
# @Author   : Ranshi
# @File     : main.py
from src.define import ListNode


# START
def check(node: ListNode) -> bool:
    flag = True
    cur = node.next
    while cur:
        if cur.val % 2 == 0:
            if flag:
                flag = False
        else:
            if not flag:
                return False
        cur = cur.next
    return True


# END
# TEST

if __name__ == '__main__':
    s = ListNode.init_list([0, 1, 3, 5, 8, 4, 2])
    print(check(s))
