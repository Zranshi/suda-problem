# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 11:24
# @Author   : Ranshi
# @File     : main.py
from pyal.container import TreeNode


# START
def is_strict_binary(node: TreeNode) -> bool:
    """
    判断一个二叉树是否严格二叉(指节点的出度只能为 0 或 2, 不存在出度为 1 的节点)

    采用递归求解.

    判断一个节点作为根节点的子树是否严格二叉的判定过程为:

    1. 若出度为 2, 则需要保证左右子树都为严格的二叉树
    2. 若出度为 1, 则不为严格二叉树.
    3. 若出度为 0, 则为严格的二叉树.

    Args:
        node (TreeNode): 输入的二叉树根节点.

    Returns:
        bool: 该二叉树是否严格二叉.
    """
    if node.left and node.right:
        return is_strict_binary(node.left) and is_strict_binary(node.right)
    elif node.left or node.right:
        return False
    return True


# END
# TEST
if __name__ == "__main__":
    tn = TreeNode.init_by_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    s = [12, 3, 1, 3, 12, 31, 23, 1]
    if tn:
        print(is_strict_binary(tn))
