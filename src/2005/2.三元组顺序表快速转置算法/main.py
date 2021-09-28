# -*- coding:utf-8 -*-
# @Time     : 2021/7/18 17: 00
# @Author   : Ranshi
# @File     : main.py
from src.define.Matrix import Triple, TSMatrix


# START
def fast_transpose(ts: TSMatrix) -> TSMatrix:
    """
    三元组顺序表快速转置算法.
    转置的算法并不复杂, 只需要互换x, y的坐标即可. 但真正困难的是将排序后的坐标排序形成顺序表.
    快速转置算法的原理是利用开始时已经排序好的三元组顺序表的信息, 在常数时间内将其放入新的三元组中.
    具体如下:
        1. 已知未排序的三元组顺序表是先根据x排序, 若x相同, 再根据y排序. 则转置后y一定是从上到下依次
           递增的, 因此我们可以利用这一点.
        2. 先遍历一遍转置后的顺序表, 记录不同的x的分组各有多少个. 将其保存至一个数组中. 这是为了
           在遍历到一个三元组时, 可以方便地知道要将其放入在什么位置.
        3. 最后便利一遍待转置的三元组顺序表, 每次将当前三元组转置后放入目标顺序表中.

    Args:
        ts (TSMatrix): 待转置的三元组顺序表

    Returns:
        TSMatrix: 转置完成的三元组顺序表
    """
    nums = [0 for _ in range(ts.nu + 1)]
    for item in ts.triple_list:
        nums[item.j] += 1
    pot = [0, 1]
    for item in nums[1:]:
        pot.append(pot[-1] + item)
    res = TSMatrix(mu=ts.nu, nu=ts.mu, tu=ts.tu)
    for triple in ts.triple_list:
        triple.i, triple.j = triple.j, triple.i
        res.triple_list[pot[triple.i] - 1] = triple
        pot[triple.i] += 1
    ts = res
    return ts


# END
# TEST
if __name__ == "__main__":
    t = TSMatrix(
        mu=6,
        nu=5,
        tu=8,
        triple_list=[
            Triple(1, 2, 12),
            Triple(1, 3, 9),
            Triple(3, 1, -1),
            Triple(3, 5, 14),
            Triple(4, 3, 24),
            Triple(5, 2, 18),
            Triple(6, 1, 15),
            Triple(6, 4, -7),
        ],
    )
    print(fast_transpose(t))
