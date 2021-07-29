# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 20:56
# @Author   : Ranshi
# @File     : main.py

from typing import List


# START
def two_order_list_median(l1: List[int], l2: List[int]) -> float:
    merge_l: List[int] = []
    flag = 'even'
    target = (len(l1) + len(l2)) // 2
    if (len(l1) + len(l2)) % 2:
        flag = 'odd'
        target += 1
    idx: int = 0
    ptr1, ptr2 = 0, 0
    while ptr1 < len(l1) and ptr2 < len(l2):
        if l1[ptr1] < l2[ptr2]:
            merge_l.append(l1[ptr1])
            ptr1 += 1
        else:
            merge_l.append(l2[ptr2])
            ptr2 += 1
        idx += 1
        if idx == target:
            break
    return merge_l[-1] if flag == 'odd' else (merge_l[-1] + merge_l[-2]) / 2


# END
# TEST
if __name__ == '__main__':
    l1 = [
        1, 2, 3, 5, 11, 12, 23, 25, 31, 34, 43, 46, 56, 67, 68, 123, 345, 412,
        423, 567, 678, 981
    ]
    l2 = [
        2, 5, 5, 12, 34, 45, 78, 123, 124, 234, 323, 345, 436, 456, 567, 568,
        568, 679, 789
    ]
    print(two_order_list_median(l1, l2))
