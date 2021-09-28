# -*- coding:utf-8 -*-
# @Time     : 2021/7/22 11: 54
# @Author   : Ranshi
# @File     : Map.py
from collections import defaultdict
from typing import Any, Dict, List, Tuple

from src.define.ListNode import LinkList


class Map(object):
    def __init__(self, value_map: Dict[Any, List[Tuple[Any]]]):
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

    def get_lines(self, node: Any):
        """
        获得当前结点的所有相邻的边
        :param node: 当前结点
        :return:
        """
        if node in self.lines:
            yield from self.lines[node]
        else:
            return None


class AdjacencyList(object):
    def __init__(self, value_map: dict) -> None:
        """构造函数，根据一个字典构造带权值有向图

        Args:
            value_map (dict): 形如：{
                    start_node : [(end_node11, cost11), (end_node12, cost12)...]
                    start_node : [(end_node21, cost21), (end_node22, cost22)...]
                    ...
                } 所表示的图
        """
        self.graph = defaultdict(LinkList)
        for key, value in value_map.items():
            for line in value:
                self.graph[key].push_tail(line[0])
                self.graph[key].head.val += 1

    def get_next_node(self, node: int):
        return self.graph[node].head.next
