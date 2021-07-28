# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 11: 54
# @Author   : Ranshi
# @File     : Matrix.py
from typing import Optional


class Triple:
    def __init__(self, i: int, j: int, value: int):
        self.i = i
        self.j = j
        self.value = value


class TSMatrix:
    def __init__(self, mu: int, nu: int, tu: int, triple_list: Optional[Triple]):
        self.mu = mu
        self.nu = nu
        self.tu = tu
        self.triple_list = triple_list