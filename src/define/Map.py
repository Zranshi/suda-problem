# -*- coding:utf-8 -*-
# @Time     : 2021/7/22 11: 54
# @Author   : Ranshi
# @File     : Map.py
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

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


class ArcNode(object):
    """
    顺序表的边节点类, 是一个链表结构的用于保存指向节点和权重的链表.
    实现了通过list初始化的功能.
    """

    def __init__(
        self, target: int = 0, weight: int = 0, next: Optional["ArcNode"] = None
    ) -> None:
        self.target = target
        self.weight = weight
        self.next = next

    @classmethod
    def init_by_list(cls, arr: List[Any]) -> Optional["ArcNode"]:
        head = ArcNode()
        cur = head
        for x in arr:
            node = ArcNode(target=x[0], weight=x[1], next=None)
            cur.next, cur = node, node
        return head.next


class VNode(object):
    """
    顺序表的节点类, 记录了当前节点的数据、出度、入度和边度单链表.
    """

    def __init__(
        self,
        data: int = 0,
        in_degree: int = 0,
        out_degree: int = 0,
        first_arc: Optional[ArcNode] = ArcNode(),
    ) -> None:
        self.data = data
        self.in_degree = in_degree
        self.out_degree = out_degree
        self.first_arc = first_arc


class ArcGraph(object):
    """
    顺序表类, 记录了边的数量和节点的数量, 以及一个节点的列表, 用于描述图的结构.
    """

    def __init__(
        self, graph: List[VNode] = [], vex: int = 0, arc: int = 0
    ) -> None:
        self.graph = graph
        self.vex_num = vex
        self.arc_num = arc
