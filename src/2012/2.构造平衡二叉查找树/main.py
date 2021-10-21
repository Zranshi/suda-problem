# -*- coding:utf-8 -*-
# @Time     : 2021/7/26 19:58
# @Author   : Ranshi
# @File     : main.py
from pyal.container import TreeNode


# START
def init_balance_search_tree(n: int) -> TreeNode:
    """
    将自然数range(1,n+1)作为树的节点的值, 构造一棵平衡二叉查找树.

    采用递归的方法, 由于自然数是递增有序的, 因此可以选择中间节点作为子树的父节点, 左边的
    元素作为左子树, 右边的节点作为右子树. 递归下去就可以构建成一颗平衡的二叉查找树.

    Args:
        n (int): 自然数.

    Returns:
        TreeNode: 平衡的二叉查找树.
    """

    def dfs(le: int, ri: int) -> TreeNode:
        mid = (le + ri) // 2
        return TreeNode(
            val=mid,
            left=dfs(le, mid - 1) if le != mid else None,
            right=dfs(mid + 1, ri) if ri != mid else None,
        )

    return dfs(1, n)


# END

# TEST
if __name__ == "__main__":
    s = init_balance_search_tree(15)
    print(s)
