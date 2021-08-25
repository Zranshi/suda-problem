# -*- coding:utf-8 -*-
# @Time     : 2021/07/31 22:47
# @Author   : Ranshi
# @File     : main.py

from typing import List


# START
def less_nums(n: int) -> List[int]:
    dp = set()

    def dfs(idx: int):
        if idx <= n and idx not in dp:
            dp.add(idx)
            dfs(idx * 2)
            dfs(idx * 3)
            dfs(idx * 5)

    dfs(1)
    return list(dp)


# END

# TEST
if __name__ == '__main__':
    print(less_nums(100))
