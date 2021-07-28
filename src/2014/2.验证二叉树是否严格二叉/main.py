# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 11:24
# @Author   : Ranshi
# @File     : main.py

import sys

sys.path.append("/Users/rs/Documents/projects/python_project/suda-problem")
from src.define import TreeNode


# START
def is_strict_binary(node: TreeNode) -> bool:
    if node.left and node.right:
        return True and is_strict_binary(node.left) and is_strict_binary(
            node.right)
    elif node.left or node.right:
        return False
    return True


# END
# TEST
if __name__ == '__main__':
    tn = TreeNode.init_by_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if tn:
        print(is_strict_binary(tn))
