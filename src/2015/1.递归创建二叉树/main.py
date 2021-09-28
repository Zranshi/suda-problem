# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 18:53
# @Author   : Ranshi
# @File     : main.py
import sys
from typing import List, Optional

sys.path.append("/Users/rs/Documents/projects/python_project/suda-problem")
from src.define import TreeNode


# START
def init_tree_by_list(chs: Optional[List[str]], idx: int = 0) -> Optional[TreeNode]:
    if chs and idx < len(chs):
        return TreeNode(
            val=chs[idx],
            left=init_tree_by_list(chs, idx * 2 + 1),
            right=init_tree_by_list(chs, idx * 2 + 2),
        )


# END

# TEST
if __name__ == "__main__":
    chs: List[str] = list("swefdsaqwddgcsf")
    node = init_tree_by_list(chs)
    if node:
        # 输出前序遍历
        print(node)
