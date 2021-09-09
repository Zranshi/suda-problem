# -*- coding:utf-8 -*-
# @Time     : 2021/07/29 17:50
# @Author   : Ranshi
# @File     : main.py
from typing import List


# START
def min_subsequence(arr: List[int]) -> int:
    res, idx = 0, 0
    for x in arr:
        idx += x
        if idx > 0:
            idx = 0
        else:
            res = min(idx, res)
    return res


# END

# TEST

if __name__ == "__main__":
    print(min_subsequence([10, 20, -10, 8, -30, 20]))
