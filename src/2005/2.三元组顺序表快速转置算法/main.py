# -*- coding:utf-8 -*-
# @Time     : 2021/7/18 17: 00
# @Author   : Ranshi
# @File     : main.py

# DEFINE
class Triple:
    def __init__(self, i: int, j: int, value: int):
        self.i = i
        self.j = j
        self.value = value


class TSMatrix:
    def __init__(self, mu, nu, tu, triple_list):
        self.mu = mu
        self.nu = nu
        self.tu = tu
        self.triple_list = triple_list


# START1
def transpose(ts: TSMatrix):
    ts.mu, ts.nu = ts.nu, ts.mu
    t_l = []
    for idx_level, item in ((x, y) for x in range(1, ts.mu + 1) for y in ts.triple_list):
        if item.j == idx_level:
            t_l.append(Triple(i=item.j, j=item.i, value=item.value))
    ts.triple_list = t_l


# END1

# START2
def fast_transpose(ts: TSMatrix):
    nums, pot = [0 for _ in range(ts.nu + 1)], [1]
    for item in ts.triple_list:
        nums[item.j] += 1
    for item in nums[1:]:
        pot.append(pot[-1] + item)
    t_l = [None] * ts.tu
    for item in ts.triple_list:
        item.i, item.j = item.j, item.i
        t_l[pot[item.i - 1] - 1] = item
        pot[item.i - 1] += 1
    ts.triple_list = t_l

# END2
