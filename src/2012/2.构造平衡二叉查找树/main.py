# -*- coding:utf-8 -*-
# @Time     : 2021/7/26 19:58
# @Author   : Ranshi
# @File     : main.py
from src.define import TreeNode


# START
def init_balance_search_tree(n: int) -> TreeNode:
    def dfs(le: int, ri: int) -> TreeNode:
        mid = (le + ri) // 2
        return TreeNode(
            val=mid,
            left=dfs(le, mid - 1) if le != mid else None,
            right=dfs(mid + 1, ri) if ri != mid else None
        )

    return dfs(1, n)


# END


# TEST
if __name__ == '__main__':
    s = init_balance_search_tree(10)
    print(s)
