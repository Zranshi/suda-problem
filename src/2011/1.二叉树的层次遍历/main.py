# -*- coding:utf-8 -*-
# @Time     : 2021/7/25 10:49
# @Author   : Ranshi
# @File     : main.py
from typing import Generator, Optional

from src.define import TreeNode

# START
def level_order(node: Optional[TreeNode]) -> Generator:
    """
    二叉树的层序遍历.

    Args:
        node (Optional[TreeNode]): 二叉树.

    Yields:
        Generator: 返回一个层序遍历二叉树的生成器.
    """
    if node is None:
        return None
    level = [node]
    while level:
        new_level = []
        for item in level:
            yield item
            if item.left:
                new_level.append(item.left)
            if item.right:
                new_level.append(item.right)
        level = new_level


# END

# TEST
if __name__ == "__main__":
    tree = TreeNode.init_by_list(
        [item if item != " " else "" for item in "123456 7 89"]
    )
    print([item.val for item in level_order(tree)])
