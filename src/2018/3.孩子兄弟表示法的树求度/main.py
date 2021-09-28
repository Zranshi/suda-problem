# coding: utf-8
# @Time     : 2021/08/11 18:10
# @Author   : Ranshi
# @File     : main.py

from src.define.Matrix import CSTreeNode


# START
def number_Kdeg(node: CSTreeNode, k: int) -> int:
    res, idx = 0, 0
    cur: CSTreeNode = node.child
    while cur:
        idx += 1
        res += number_Kdeg(cur, k)
        cur = cur.next_sibling
    if idx == k:
        res += 1
    return res


# END
# TEST

if __name__ == "__main__":
    ...
