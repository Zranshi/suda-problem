# coding: utf-8
# @Time     : 2021/08/11 17:53
# @Author   : Ranshi
# @File     : main.py
from src.define import TreeNode


class SizeTree(TreeNode):
    def __init__(self, val, left, right) -> None:
        super().__init__(val, left=left, right=right)
        self.size = 0

    @classmethod
    def init_by_list(cls, arr: list, idx: int = 0):
        """
        使用列表初始化一个二叉树
        :param arr:
        :param idx:
        :return:
        """
        if idx < len(arr) and arr[idx]:
            return SizeTree(
                val=arr[idx],
                left=SizeTree.init_by_list(arr, idx * 2 + 1),
                right=SizeTree.init_by_list(arr, idx * 2 + 2),
            )


# START
def add_size(root: SizeTree) -> int:
    if root.left:
        root.size += add_size(root.left) + 1
    if root.right:
        root.size += add_size(root.right) + 1
    return root.size


# END
# TEST

if __name__ == "__main__":
    st = SizeTree.init_by_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if st:
        print(add_size(st))
