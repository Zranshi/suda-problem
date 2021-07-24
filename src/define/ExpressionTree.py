# -*- coding:utf-8 -*-
# @Time     : 2021/7/24 10: 49
# @Author   : Ranshi
# @File     : ExpressionTree.py

class ExpressionTree:
    def __init__(self, val, left: 'ExpressionTree' = None, right: 'ExpressionTree' = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def init_str(cls, s: str) -> 'ExpressionTree':
        """
        使用字符串初始化二叉树
        :param s:
        :return:
        """

        def init(idx: int) -> ExpressionTree:
            if s[idx] != ' ':
                return ExpressionTree(
                    val=s[idx],
                    left=init(idx * 2 + 1) if idx * 2 + 1 < len(s) else None,
                    right=init(idx * 2 + 2) if idx * 2 + 2 < len(s) else None
                )

        return init(0)

    def __str__(self):
        res = []

        def preOrder(idx_root: ExpressionTree):
            res.append(idx_root.val)
            if idx_root.left:
                preOrder(idx_root.left)
            if idx_root.right:
                preOrder(idx_root.right)

        preOrder(self)
        return ''.join(res)