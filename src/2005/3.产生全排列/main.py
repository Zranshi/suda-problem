# -*- coding:utf-8 -*-
# @Time     : 2021/7/18 17: 20
# @Author   : Ranshi
# @File     : main.py
from typing import List


# START
def permutations(lst: list) -> List[int]:
    """
    输出数组的全排列.
    使用dfs算法输出数组的全排列.
    在每次调用函数时, for循环遍历所有arr[le]的情况, 然后递归去寻找 (le+1, ri)的全排列.
    直到le==ri, 则保存当前的arr为一个排列.
    这是一种自顶向下的实现方法.

    Args:
        lst (list): 输入的数组

    Returns:
        List[int]: 全排列的结果
    """
    res = []

    def dfs(arr: list, le: int, ri: int):
        if le == ri:
            res.append(arr[:])
        else:
            i = le
            for num in range(le, ri):
                arr[num], arr[i] = arr[i], arr[num]
                dfs(arr, le + 1, ri)
                arr[num], arr[i] = arr[i], arr[num]

    dfs(lst, 0, len(lst))
    return res


# END

# TEST
if __name__ == '__main__':
    test_arr = [1, 2, 3]
    for i in permutations(test_arr):
        print(i)
