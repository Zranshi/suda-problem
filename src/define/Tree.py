# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 11: 55
# @Author   : Ranshi
# @File     : Tree.py

from collections import deque
from typing import Any, List, Optional


class TreeNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def init_by_list(
        cls,
        arr: List[Any],
        idx: int = 0,
    ) -> Optional["TreeNode"]:
        """
        使用列表初始化一个二叉树
        :param arr:
        :param idx:
        :return:
        """
        if idx < len(arr) and arr[idx]:
            return TreeNode(
                val=arr[idx],
                left=TreeNode.init_by_list(arr, idx * 2 + 1),
                right=TreeNode.init_by_list(arr, idx * 2 + 2),
            )

    @classmethod
    def init_balanced_sort_tree(cls, arr: List[Any]):
        lst = sorted(arr)

        def dfs(le: int, ri: int) -> TreeNode:
            mid = (le + ri) // 2
            return TreeNode(
                val=lst[mid],
                left=dfs(le, mid - 1) if le != mid else None,
                right=dfs(mid + 1, ri) if ri != mid else None,
            )

        return dfs(0, len(lst) - 1)

    def __str__(self) -> str:
        level = [self]
        res = []
        while any(level):
            res.append(
                " ".join(f"{item.val:<4}" if item else "None" for item in level)
            )
            next_level = [None] * len(level) * 2
            for i, item in enumerate(level):
                next_level[i * 2] = item.left if item and item.left else None
                next_level[i * 2 + 1] = (
                    item.right if item and item.right else None
                )
            level = next_level
        return "\n".join(res)


class CSTreeNode:
    def __init__(self, val, child, next_sibling) -> None:
        """
        采用孩子兄弟法存储的树结构
        :param val: 数据域
        :param child: 孩子指针
        :param next_sibling: 兄弟指针
        """
        self.val = val
        self.child = child
        self.next_sibling = next_sibling

    def __str__(self) -> str:
        res = []

        def dfs(idx: CSTreeNode):
            if idx:
                res.append(str(idx.val))
                if idx.next_sibling:
                    dfs(idx.next_sibling)
                if idx.child:
                    dfs(idx.child)

        return " ".join(res)


class SearchTree(TreeNode):
    def __init__(
        self,
        val: int,
        left: Optional["SearchTree"] = None,
        right: Optional["SearchTree"] = None,
        r_size: int = 1,
    ) -> None:
        TreeNode.__init__(self, val, left, right)
        self.r_size = r_size


if __name__ == "__main__":
    l1 = [i for i in range(1, 50)]
    tr = SearchTree.init_by_list(l1)
    print(tr)
