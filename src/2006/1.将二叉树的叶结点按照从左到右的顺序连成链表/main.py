# -*- coding:utf-8 -*-
# @Time     : 2021/7/18 20: 40
# @Author   : Ranshi
# @File     : main.py
from src.define import LinkList, TreeNode


# START1
def leaves_list(tree: TreeNode) -> LinkList:
    """
    栈实现
    :param tree:
    :return:
    """
    head = LinkList()
    stack = [tree]
    while stack:
        idx = stack.pop()
        if not idx.left and not idx.right:
            head.push_tail(idx.val)
            continue
        if idx.right:
            stack.append(idx.right)
        if idx.left:
            stack.append(idx.left)
    return head


# EDN1


# START2
def leaves_list_rec(tree: TreeNode) -> LinkList:
    """
    递归实现
    :param tree:
    :return:
    """
    head = LinkList()

    def dfs(root: TreeNode):
        if not root.left and not root.right:
            head.push_tail(root.val)
        else:
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

    dfs(tree)
    return head


# END2

# TEST
if __name__ == '__main__':
    tn = TreeNode.init_by_list(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, 10, 11, 12])
    if tn:
        print(leaves_list(tn))
