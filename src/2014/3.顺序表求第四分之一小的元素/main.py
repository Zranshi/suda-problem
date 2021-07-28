# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 15:58
# @Author   : Ranshi
# @File     : main.py

from typing import List

# START


def get_quarter(arr: List[int], lo: int = 0, hi: int = None) -> int:
    k = len(arr) // 4
    if not hi:
        hi = len(arr) - 1
    if lo < hi and len(arr) >= 4:
        key = arr[lo]
        left, right = lo, hi
        while left < right:
            while left < right and key < arr[right]:
                right -= 1
            arr[left] = arr[right]
            while left < right and key > arr[left]:
                left += 1
            arr[right] = arr[left]
        arr[left] = key
        if left == k:
            return arr[left]
        elif left < k:
            return get_quarter(arr, left + 1, hi)
        else:
            return get_quarter(arr, lo, left)
    else:
        return -1


def get_q(arr: List[int]) -> int:
    arr.sort()
    print(arr)
    return arr[len(arr) // 4]


# END

# TEST
if __name__ == '__main__':
    arr: List[int] = [1, 24, 2, 45, 6, 56, 7, 33, 35, 42, 16, 23]
    # print(get_q(arr))
    print(get_quarter(arr))
