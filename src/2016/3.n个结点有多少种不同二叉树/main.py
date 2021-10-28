# -*- coding:utf-8 -*-
# @Time     : 2021/07/31 21:22
# @Author   : Ranshi
# @File     : main.py
# START
from functools import lru_cache


@lru_cache()
def n_node_tree_num(n: int) -> int:
    """
    n 个结点可以有多少种不同的二叉树.

    由于该问题具有重复子结构的特性, 具体为

    f(n) = f(0)*f(n-1) + f(1)*f(n-2) ... f(n-2)*f(1) + f(n-1)*f(0)

    由于题目要求使用递归函数的形式编写, 而若是普通递归会造成大量的重复计算, 因此采用
    Python的函数缓存, 将函数结果保存下载, 避免重复计算.

    Args:
        n (int): n 个结点.

    Returns:
        int: 可以构成的二叉树个数.
    """
    if n == 0:
        return 1
    return sum(n_node_tree_num(i) * n_node_tree_num(n - i - 1) for i in range(n))


# END

# TEST
if __name__ == "__main__":
    for i in range(1, 20):
        print(n_node_tree_num(i))
