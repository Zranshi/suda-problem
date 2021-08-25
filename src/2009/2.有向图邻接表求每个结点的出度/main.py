# -*- coding:utf-8 -*-
# @Time     : 2021/7/23 16: 42
# @Author   : Ranshi
# @File     : main.py
from src.define import Map


# START
def get_out_degree(m: Map) -> dict:
    return {point: len(m.lines[point]) for point in m.lines}


# END

# TEST
if __name__ == '__main__':
    test_map = {
        1: [(2, 4), (3, 3)],
        2: [(4, 8), (5, 6)],
        3: [(5, 7), (6, 8)],
        4: [(7, 3)],
        5: [(8, 1), (4, 1)],
        6: [(8, 9)],
        7: [(8, 2)],
        8: []
    }
    m = Map(value_map=test_map)
    print(get_out_degree(m))
