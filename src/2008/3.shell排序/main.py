# -*- coding:utf-8 -*-
# @Time     : 2021/7/22 12: 54
# @Author   : Ranshi
# @File     : main.py

# START
from typing import List


def shell_sort(arr: List[int]) -> List[int]:
    """
    希尔排序.

    Args:
        arr (List[int]): 待排序数组.

    Returns:
        List[int]: 排序完成后的数组.
    """
    length = len(arr)
    for sub in range(length // 2, 0, -1):
        for idx in range(0, length, sub):
            min_idx = idx
            for i in range(idx, length, sub):
                if arr[i] < arr[min_idx]:
                    min_idx = i
            arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    return arr


# END

# TEST
if __name__ == "__main__":
    nums = [34, 5, 12, 1, 4, 6, 7, 8, 67, 2, 87, 3, 55]
    print(shell_sort(nums))
