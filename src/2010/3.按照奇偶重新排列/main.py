# -*- coding:utf-8 -*-
# @Time     : 2021/7/24 11: 49
# @Author   : Ranshi
# @File     : main.py

from typing import List


# START
def com_even_odd(arr: List[int]) -> List[int]:
    odd, even, idx = 1, 0, 0
    while idx < len(arr) and odd < len(arr) and even < len(arr):
        if arr[idx] % 2 == 1 and idx > odd:
            arr[idx], arr[odd] = arr[odd], arr[idx]
            odd += 2
        elif arr[idx] % 2 == 0 and idx > even:
            arr[idx], arr[even] = arr[even], arr[idx]
            even += 2
        idx += 1
    return arr


# END

# TEST
if __name__ == '__main__':
    print(com_even_odd([2, 2, 21, 1, 2, 2, 2, 2, 2, 2]))
