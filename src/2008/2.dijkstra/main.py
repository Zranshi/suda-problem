# -*- coding:utf-8 -*-
# @Time     : 2021/7/22 11: 53
# @Author   : Ranshi
# @File     : main.py
from src.define import Map


# START
def dijkstra(target_map: Map, node: int):
    point_dict = {node: 0}  # 表示起始点到目标点的最小路径长度
    pre_node = {node: node}  # 记录路径中的前驱
    v = {node}  # 记录节点是否已经有了最短路径

    for line_node, line_cost in target_map.get_lines(node):
        # 先将起始点能直接遍历到的点记入dict中
        point_dict[line_node] = line_cost
        pre_node[line_node] = node

    for _ in range(target_map.size - 1):
        cost, min_node = float("inf"), None  # 寻找当前最小路径的点
        for index_node, value in point_dict.items():
            if index_node not in v and cost > value:
                cost = point_dict[index_node]
                min_node = index_node

        v.add(min_node)

        for line_node, line_cost in target_map.get_lines(min_node):  # 更新dict
            if (
                line_node not in point_dict
                or point_dict[line_node] > line_cost + cost
            ):
                point_dict[line_node] = line_cost + cost
                pre_node[line_node] = min_node

    return format_res(point_dict, pre_node)


def format_res(cost, pre):
    res_dict = {}
    for node in cost:
        res_dict[node] = {"cost": cost[node]}
        path = [str(node)]
        idx = node
        while pre[idx] != idx:
            idx = pre[idx]
            path.append(str(idx))
        res_dict[node]["path"] = "->".join(path[::-1])
    return res_dict


# END

# TEST
if __name__ == "__main__":
    test_map = {
        1: [(2, 4), (3, 3)],
        2: [(4, 8), (5, 6)],
        3: [(5, 7), (6, 8)],
        4: [(7, 3)],
        5: [(8, 1), (4, 1)],
        6: [(8, 9)],
        7: [(8, 2)],
        8: [],
    }
    m = Map(value_map=test_map)
    print(dijkstra(m, 1))
