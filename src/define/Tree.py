# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 11: 55
# @Author   : Ranshi
# @File     : Tree.py


class TreeNode:
    def __init__(self, val, left: 'TreeNode' = None, right: 'TreeNode' = None):
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


class CSTreeNode:
    def __init__(self, val, child: 'CSTreeNode' = None, next_sibling: 'CSTreeNode' = None):
        """
        采用孩子兄弟法存储的树结构
        :param val: 数据域
        :param child: 孩子指针
        :param next_sibling: 兄弟指针
        """
        self.val = val
        self.child = child
        self.next_sibling = next_sibling

    def __str__(self):
        res = []

        def dfs(idx: CSTreeNode):
            if idx:
                res.append(str(idx.val))
                if idx.next_sibling:
                    dfs(idx.next_sibling)
                if idx.child:
                    dfs(idx.child)

        return ' '.join(res)
