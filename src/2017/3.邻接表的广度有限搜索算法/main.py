# -*- coding:utf-8 -*-
# @Time     : 2021/08/02 10:36
# @Author   : Ranshi
# @File     : main.py
from src.define import AdjacencyList
from typing import List

# START
def bfs(ad_list: AdjacencyList, start: int, end: int) -> bool:
    """
    使用广度优先算法搜索用邻接表实现的有向图是否存在一条从 start 出发, 到 end 结束的路径.

    简单的广度优先搜索, 比较困难的反而是构建数据结构并初始化一个图.

    Args:
        ad_list (AdjacencyList): 用邻接表实现的有向图.
        start (int): 出发点.
        end (int): 终点.

    Returns:
        bool: 是否存在这样一条路径.
    """
    from collections import deque

    dq = deque()
    dq.appendleft(start)
    path = set()
    while dq:
        idx = dq.pop()
        if idx == end:
            return True
        next_node = ad_list.get_next_node(idx)
        while next_node:
            if next_node not in path:
                dq.appendleft(next_node.val)
                path.add(next_node)
            next_node = next_node.next
    return False


# END
# TEST

if __name__ == "__main__":
    ad = AdjacencyList(
        value_map={
            1: [(2, 4), (3, 3)],
            2: [(4, 8), (5, 6)],
            3: [(5, 7), (6, 8)],
            4: [(7, 3)],
            5: [(8, 1), (4, 1)],
            6: [(8, 9)],
            7: [(8, 2)],
            8: [],
        }
    )
    print(bfs(ad_list=ad, start=1, end=8))
