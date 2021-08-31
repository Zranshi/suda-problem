# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 11: 54
# @Author   : Ranshi
# @File     : Matrix.py
from typing import List


class Triple:

    def __init__(self, i: int = 0, j: int = 0, value: int = 0):
        self.i = i
        self.j = j
        self.value = value


class TSMatrix:

    def __init__(
        self,
        mu: int,
        nu: int,
        tu: int,
        triple_list: List[Triple] = [],
    ):
        self.mu = mu
        self.nu = nu
        self.tu = tu
        self.triple_list = triple_list if triple_list else [
            Triple() for _ in range(tu)
        ]

    def __str__(self) -> str:
        res = []
        res.append(f'm: {self.mu}, n: {self.nu}, element: {self.tu}')
        for triple in self.triple_list:
            res.append(f'{triple.i}, {triple.j}, {triple.value}')
        return '\n'.join(res)
