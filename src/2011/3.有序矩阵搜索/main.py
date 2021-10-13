# -*- coding:utf-8 -*-
# @Time     : 2021/7/25 11:31
# @Author   : Ranshi
# @File     : main.py
from typing import List


# START
def matrix_search(arr: List[List[int]], target: int) -> bool:
    """
    有序二维数组中查找目标值.

    由于是在行递增, 列递减的二维数组中, 因此我们可以将初始点位于第一行的最后一列中,
    然后判断其是否与目标值相等:

    - 如果相等则退出
    - 如果大于, 则减少列数
    - 如果小于, 则增加行数

    因此可以遍历到二维数组中所有的数.

    Args:
        arr (List[List[int]]): 有序二维数组.
        target (int): 目标值.

    Returns:
        bool: 是否存在.
    """
    row, col = len(arr), len(arr[0])
    i, j = 0, col - 1
    while i < row and col >= 0:
        idx = arr[i][j]
        if idx == target:
            return True
        elif idx > target:
            j -= 1
        else:
            i += 1
    return False


# EMD

# TEST
if __name__ == "__main__":
    print(
        matrix_search(
            arr=[
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            target=9,
        )
    )
