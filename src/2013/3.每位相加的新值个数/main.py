# -*- coding:utf-8 -*-
# @Time     : 2021/7/27 10:11
# @Author   : Ranshi
# @File     : main.py
def get_number(n: int) -> int:
    """
    输入一个数, 返回它通过一种运算可以得到所有正整数的个数.

    这种运算的规则是, 对于这个数 n , 可以在其前加一个小于等于 n 一半的数 m , 来构成一个新的数 mn
    , 对于 mn , 可以递归取得一个小于等于 m 一半的数 p, 构成一个新的数 pmn. 依次递推.

    解决方法:
    使用动态规划的思想, 由底至上的递归方法. 因为我们可以看出, 该运算具有重复子结构, 因此可以依次
    取得1-n的所有数的可以得到的个数.

    由于使用了一个 pre 变量来保存需要的前序和, 因此实际上的时间复杂度为O(n), 由于需要大小为 n 的
    数组来保存之前的数据, 因此空间复杂度为O(n).

    Args:
        n (int): 输入的数.

    Returns:
        int: 通过这种运算可以得到正整数的个数.
    """
    dp = [0] * (n + 1)
    pre = 0
    for i in range(1, n + 1):
        if i & 1 == 0:
            pre += dp[i >> 1]
        dp[i] = 1 + pre
    return dp[n]


# END

# TEST
if __name__ == "__main__":
    print(get_number(8))
    print(get_number(2001))
