# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 12: 22
# @Author   : Ranshi
# @File     : main.py
import heapq


# START
def longest_path(_map: dict, start: int = 0):
    """
    求DAG的单源最长路径.

    可以转换成求所有权值为相反数的最短路径. 最短路径可以使用Dijkstra求出.

    Args:
        _map (dict): DAG
    """
    length = [float("inf") for _ in range(len(_map))]
    pre = [start for _ in range(len(_map))]
    que = [[-v[0], v[1], v[2]] for v in _map[start]]
    heapq.heapify(que)

    for _ in range(len(_map) - 1):
        idx_len, idx_node, idx_pre = heapq.heappop(que)
        length[idx_node] = idx_len
        pre[idx_node] = idx_pre
        for v in _map[idx_node]:
            heapq.heappush(que, [-v[0] + idx_len, v[1], v[2]])

    max_node = start
    for i in range(len(length)):
        if length[i] < length[max_node]:
            max_node = i

    print(f"The longest path length is {-length[max_node]}")

    path = [str(max_node)]
    while pre[max_node] != max_node:
        max_node = pre[max_node]
        path.append(str(max_node))
    path_str = "->".join(path[::-1])
    print(f"The path is {path_str}")


# END

# TEST
if __name__ == "__main__":
    m = {
        0: [[1, 3, 0], [2, 1, 0]],
        1: [[2, 3, 1], [3, 2, 1], [4, 4, 1]],
        2: [[3, 4, 2]],
        3: [[4, 4, 3], [5, 5, 3]],
        4: [[5, 5, 4]],
        5: [],
    }
    longest_path(_map=m)
