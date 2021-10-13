# -*- coding:utf-8 -*-
# @Time     : 2021/7/24 11: 49
# @Author   : Ranshi
# @File     : main.py

from typing import List


# START
def com_even_odd(arr: List[int]) -> List[int]:
    """
    让所有的偶数位于数组的偶数下标上, 或者所有奇数位于数组的奇数下标上.

    由于一个整数必定是偶数或是奇数, 因此只需要让偶数/奇数其中一个排列正确, 则能保证满足题意.
    因此我选择修改偶数下标, 用两个指针分别指向了偶数下标和奇数下标, 并不断找到不符合题意的元
    素, 然后交换. 直到两个指针的其中一者超过属猪边界.


    Args:
        arr (List[int]): 数组

    Returns:
        List[int]: 重新排列后的数组
    """
    even, idx = 0, 1
    while even < len(arr) and idx < len(arr):
        while even < len(arr) and not arr[even] % 2:
            even += 2

        while idx < len(arr) and arr[idx] % 2:
            idx += 2

        if idx < len(arr) and even < len(arr):
            arr[idx], arr[even] = arr[even], arr[idx]
    return arr


# END

# TEST
if __name__ == "__main__":
    print(com_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))
