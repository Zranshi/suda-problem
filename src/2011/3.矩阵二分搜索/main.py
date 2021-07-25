# -*- coding:utf-8 -*-
# @Time     : 2021/7/25 11:31
# @Author   : Ranshi
# @File     : main.py
from typing import List


# START
def matrix_search(arr: List[List[int]], target: int) -> bool:
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
if __name__ == '__main__':
    print(matrix_search(
        arr=[
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ],
        target=9
    ))
