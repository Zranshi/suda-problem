# -*- coding:utf-8 -*-
# @Time     : 2021/07/29 17:50
# @Author   : Ranshi
# @File     : main.py

# START
def min_subsequence(arr: list[int]) -> int:
    """
    求顺序表中连续序列的最小值.

    和求连续序列的最大值相同的做法, 只需要遍历一次顺序表, 在遍历过程中, 记录当前总和,
    如果大于零则丢弃前面的序列, 因为大于零的之前的序列无法在最后获得最小值.

    Args:
        arr (List[int]): 顺序表

    Returns:
        int: 顺序表中连续序列的最小值.
    """
    res, idx = 0, 0
    for x in arr:
        idx += x
        if idx > 0:
            idx = 0
        else:
            res = min(idx, res)
    return res


# END

# TEST

if __name__ == "__main__":
    print(min_subsequence([10, 20, -10, 8, -30, 20]))
