# -*- coding:utf-8 -*-
# @Time     : 2021/7/20 12: 14
# @Author   : Ranshi
# @File     : main.py
from src.define import TreeNode


# START
def insert_node(tree: TreeNode, target: TreeNode):
    """
    将一个节点插入到二叉排序树中.

    Args:
        tree (TreeNode): 二叉排序树
        target (TreeNode): 目标节点
    """
    if target.val == tree.val:
        return
    elif target.val < tree.val:
        if tree.left:
            insert_node(tree.left, target)
        else:
            tree.left = target
    elif tree.right:
        insert_node(tree.right, target)
    else:
        tree.right = target


def merge_search_tree(tree: TreeNode, target: TreeNode) -> TreeNode:
    """
    合并两个二叉排序树.

    后序遍历第二个二叉排序树, 对于遍历到的每个节点, 将其作为单个节点插入到第一个二叉排序树中,
    然后返回第一个二叉排序树.

    Args:
        tree (TreeNode): 第一个二叉排序树
        target (TreeNode): 二个二叉排序树

    Returns:
        TreeNode: 合并后的二叉排序树
    """

    def post_order(idx: TreeNode):
        """
        后序遍历

        Args:
            idx (TreeNode): 遍历的当前节点
        """
        if idx.left:
            post_order(idx.left)
        if idx.right:
            post_order(idx.right)
        idx.left, idx.right = None, None
        insert_node(tree, idx)

    post_order(target)
    return tree


# END
# TEST

if __name__ == "__main__":

    st1 = TreeNode.init_balanced_sort_tree(
        [23, 24, 34, 678, 41, 43, 4523, 45, 434, 56, 64, 75]
    )
    st2 = TreeNode.init_balanced_sort_tree(
        [2, 3, 4, 5, 6, 7, 8, 32, 12, 23, 35, 675, 76, 65, 56]
    )
    print(st1)
    print(st2)
    print(merge_search_tree(st1, st2))
