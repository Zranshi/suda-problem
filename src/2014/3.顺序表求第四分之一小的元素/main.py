# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 15:58
# @Author   : Ranshi
# @File     : main.py
from typing import List


# START
def get_quarter(arr: List[int], lo: int = 0, hi: int = 0) -> int:
    """
    求顺序表中第 1/4 小的元素.

    最优算法: 一次快速排序分组 + 二分
    基本思路如下: 通过一趟快速排序将整个顺序表分为两部分, 然后根据分界点的位置判定下次
    分组是在哪一组或者是否得到答案. 这样可以最小地比较顺序表中的元素, 就得到答案.

    Args:
        arr (List[int]): 顺序表
        lo (int, optional): 左区间. Defaults to 0.
        hi (int, optional): 右区间. Defaults to 0.

    Returns:
        int: 第 1/4 小的元素.
    """
    # 初始化变量
    k = len(arr) // 4
    if not hi:
        hi = len(arr) - 1
    if lo >= hi or len(arr) < 4:
        return -1
    key = arr[lo]
    left, right = lo, hi

    # 进行快速排序的一次遍历
    while left < right:
        while left < right and key < arr[right]:
            right -= 1
        arr[left] = arr[right]
        while left < right and key > arr[left]:
            left += 1
        arr[right] = arr[left]
    arr[left] = key

    # 二分
    if left == k:
        return arr[left]
    elif left < k:
        return get_quarter(arr, left + 1, hi)
    else:
        return get_quarter(arr, lo, left)


# END

# TEST
if __name__ == "__main__":
    arr: List[int] = [1, 24, 2, 45, 6, 56, 7, 33, 35, 42, 16, 23]
    print(get_quarter(arr))
