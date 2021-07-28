# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 09:48
# @Author   : Ranshi
# @File     : main.py

import sys

sys.path.append("/Users/rs/Documents/projects/python_project/suda-problem")
from typing import Optional

from src.define import ListNode


# START
def get_prime_factor(num: int) -> Optional["ListNode"]:
    head = ListNode()
    cur, idx = head, num // 2
    while num > 1 and idx > 1:
        if num % idx == 0:
            for i in range(2, idx // 2 + 1):
                if idx % i == 0:
                    break
            else:
                cur.next = ListNode(idx)
                cur, num = cur.next, num // idx
                idx += 1
        idx -= 1
    return head.next


# END
# TEST
if __name__ == "__main__":
    ln = get_prime_factor(2100)
    print(ln)
