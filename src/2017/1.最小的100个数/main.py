# -*- coding:utf-8 -*-
# @Time     : 2021/07/31 22:47
# @Author   : Ranshi
# @File     : main.py

from typing import List


# START
def less_nums(n: int) -> List[int]:
    """
    一个序列有如下性质:
    1. 1 在序列中.
    2. 如果x在序列中, 那么2*x, 3*x, 5*x也在序列中.
    求这个序列中最小的n个数字.

    Args:
        n (int): 输入.

    Returns:
        List[int]: 序列中最小的n个数字.
    """
    res = [1]

    def dfs(idx: int):
        if any(not idx % item for item in [2, 3, 5]):
            res.append(idx)
            nonlocal n
            n -= 1
        if n != 1:
            dfs(idx + 1)

    dfs(1)
    return res


# END

# TEST
if __name__ == "__main__":
    print(less_nums(100))
