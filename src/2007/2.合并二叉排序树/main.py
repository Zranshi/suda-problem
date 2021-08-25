# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 12: 14
# @Author   : Ranshi
# @File     : main.py
from src.define import TreeNode


# START
def insert_node(tree: TreeNode, target: TreeNode):
    if target.val == tree.val:
        return
    elif target.val < tree.val:
        if tree.left:
            insert_node(tree.left, target)
        else:
            tree.left = target
    else:
        if tree.right:
            insert_node(tree.right, target)
        else:
            tree.right = target


def merge_search_tree(tree: TreeNode, target: TreeNode):
    def post_order(idx: TreeNode):
        if idx.left:
            post_order(idx.left)
        if idx.right:
            post_order(idx.right)
        idx.left, idx.right = None, None
        insert_node(tree, idx)

    post_order(target)

# END
