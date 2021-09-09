# -*- coding:utf-8 -*-
# @Time     : 2021/7/18 20: 40
# @Author   : Ranshi
# @File     : main.py
from src.define import TreeNode


# START
def leaves_list(tree: TreeNode) -> list:
    """
    二叉树叶结点放入动态分配顺序存储结构的顺序表.
    采用dfs算法搜索从左到右搜索叶结点.
    由于python的list本身就为动态分配的顺序存储结构, 其他语言需要在加入新元素后扩大容量
    每次扩大为当前容量大两倍.

    Args:
        tree (TreeNode): 树根节点.

    Returns:
        list: 动态分配的保存叶结点顺序存储结构.
    """
    head = []

    def dfs(root: TreeNode):
        if not root.left and not root.right and root.val != -1:
            head.append(root.val)
        else:
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

    dfs(tree)
    return head


# END

# TEST
if __name__ == "__main__":
    tn = TreeNode.init_by_list(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, 10, 11, 12]
    )
    if tn:
        print(leaves_list(tn))
