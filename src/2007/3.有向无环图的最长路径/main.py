# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 12: 22
# @Author   : Ranshi
# @File     : main.py


# START
def longest_path(_map: dict):
    """
    使用拓扑排序，队列中保存当前结点和当前路径长度，如果没有下一个结点则更新res
    :param _map:
    :return:
    """
    from collections import deque
    dq = deque()
    length = len(_map)
    res = 0
    points = [0 for _ in range(length + 1)]
    for key in _map:
        for point in _map[key]:
            points[point] += 1
    for i in range(1, length + 1):
        if points[i] == 0:
            dq.appendleft((i, 0))
    while dq:
        idx, path = dq.pop()
        if not _map[idx]:
            res = max(res, path)
        else:
            for item in _map[idx]:
                points[item] -= 1
                if points[item] == 0:
                    dq.appendleft((item, path + 1))
    return res


# END

# TEST
if __name__ == '__main__':
    m = {1: [2, 3, 4], 2: [3], 3: [4, 5], 4: [5], 5: []}
    print(longest_path(_map=m))
