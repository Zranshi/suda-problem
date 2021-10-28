# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 16: 42
# @Author   : Ranshi
# @File     : main.py
from src.define import ArcGraph, ArcNode, VNode


# START
def get_in_and_out(g: ArcGraph):
    """根据顺序表的结构, 初始化每个节点的出度和入读."""
    for line in g.graph:
        p = line.first_arc
        while p:
            line.out_degree += 1
            g.graph[p.target - 1].in_degree += 1
            p = p.next


# END

# TEST
if __name__ == "__main__":
    m = ArcGraph(
        arc=11,
        vex=8,
        graph=[
            VNode(data=23, first_arc=ArcNode.init_by_list([(2, 4), (3, 3)])),
            VNode(data=45, first_arc=ArcNode.init_by_list([(4, 8), (5, 6)])),
            VNode(data=73, first_arc=ArcNode.init_by_list([(5, 7), (6, 8)])),
            VNode(data=13, first_arc=ArcNode.init_by_list([(7, 3)])),
            VNode(data=67, first_arc=ArcNode.init_by_list([(8, 1), (4, 1)])),
            VNode(data=45, first_arc=ArcNode.init_by_list([(8, 9)])),
            VNode(data=63, first_arc=ArcNode.init_by_list([(8, 2)])),
            VNode(data=74, first_arc=ArcNode.init_by_list([])),
        ],
    )
    get_in_and_out(m)
