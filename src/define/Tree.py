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
    ) -> Optional['TreeNode']:
        """
        使用列表初始化一个二叉树
        :param arr:
        :param idx:
        :return:
        """
        if idx < len(arr) and arr[idx]:
            new_node = TreeNode(
                val=arr[idx],
                left=TreeNode.init_by_list(arr, idx * 2 + 1),
                right=TreeNode.init_by_list(arr, idx * 2 + 2),
            )
            return new_node

    def __str__(self) -> str:
        dq = deque()
        level_node: List[List[str]] = [[]]
        dq.appendleft((self, 0))
        while dq:
            idx, idx_level = dq.pop()
            if idx_level >= len(level_node):
                level_node.append([])
            if idx:
                level_node[idx_level].append(str(idx.val))
                dq.appendleft((idx.left, idx_level + 1))
                dq.appendleft((idx.right, idx_level + 1))
        return '\n'.join(' '.join(item) for item in level_node)


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

        return ' '.join(res)


class SearchTree(TreeNode):

    def __init__(
        self,
        val: int,
        left: Optional['SearchTree'] = None,
        right: Optional['SearchTree'] = None,
        r_size: int = 1,
    ) -> None:
        TreeNode.__init__(self, val, left, right)
        self.r_size = r_size


if __name__ == '__main__':
    l1 = [i for i in range(1, 50)]
    tr = SearchTree.init_by_list(l1)
    print(tr)
