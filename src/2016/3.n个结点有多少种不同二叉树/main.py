# -*- coding:utf-8 -*-
# @Time     : 2021/07/31 21:22
# @Author   : Ranshi
# @File     : main.py


# START
def n_node_tree_num(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        for j in range(0, i // 2):
            dp[i] += 2 * (dp[j] * dp[i - j - 1])
        if i % 2 == 1:
            dp[i] += dp[i // 2] ** 2
    return dp[-1]


# END

# TEST
if __name__ == '__main__':
    print(n_node_tree_num(4))
