# -*- coding:utf-8 -*-
# @Time     : 2021/7/22 11: 54
# @Author   : Ranshi
# @File     : Map.py
from typing import Dict, List, Tuple


class Map:
    def __init__(self, value_map):
        """
        构造函数，根据一个字典构造带权值有向图
        :param value_map: 形如：{
            start_node : [(end_node11, cost11), (end_node12, cost12)...]
            start_node : [(end_node21, cost21), (end_node22, cost22)...]
            ...
        }
        """
        self.size = len(value_map)
        self.lines = value_map

    def get_lines(self, node):
        """
        获得当前结点的所有相邻的边
        :param node: 当前结点
        :return:
        """
        if node in self.lines:
            for line in self.lines[node]:
                yield line
        else:
            return None
