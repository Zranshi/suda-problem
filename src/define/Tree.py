# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 11: 55
# @Author   : Ranshi
# @File     : Tree.py
from typing import Iterable


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def init_by_list(cls, arr: list, idx: int = 0) -> 'TreeNode':
        """
        使用列表初始化一个二叉树
        :param arr:
        :param idx:
        :return:
        """
        if idx < len(arr) and arr[idx]:
            newNode = TreeNode(
                val=arr[idx],
                left=TreeNode.init_by_list(arr, idx * 2 + 1),
                right=TreeNode.init_by_list(arr, idx * 2 + 2),
            )
            return newNode

    def __str__(self):
        res = []

        def preOrder(idx_root: TreeNode):
            res.append(str(idx_root.val))
            if idx_root.left:
                preOrder(idx_root.left)
            if idx_root.right:
                preOrder(idx_root.right)

        preOrder(self)
        return ' '.join(res)
