# -*- coding:utf-8 -*-
# @Time     : 2021/07/28 20:56
# @Author   : Ranshi
# @File     : main.py
# START
# def two_order_list_median(list1: List[int], list2: List[int]) -> float:
#     merge_l: List[int] = []
#     flag = "even"
#     target = (len(list1) + len(list2)) // 2
#     if (len(list1) + len(list2)) % 2:
#         flag = "odd"
#         target += 1
#     idx: int = 0
#     ptr1, ptr2 = 0, 0
#     while ptr1 < len(list1) and ptr2 < len(list2):
#         if list1[ptr1] < list2[ptr2]:
#             merge_l.append(list1[ptr1])
#             ptr1 += 1
#         else:
#             merge_l.append(list2[ptr2])
#             ptr2 += 1
#         idx += 1
#         if idx == target:
#             break
#     return merge_l[-1] if flag == "odd" else (merge_l[-1] + merge_l[-2]) / 2


def two_order_list_median(lst1: list[int], lst2: list[int]) -> float:
    """
    二分法求解.

    对于两个有序数组, 可以划分为两部分, 一部分小于等于中位数, 一部分大于中位数. 而中位数
    就可以在这条边界旁取得. 因此我们可以通过二分的方法分别在两个数组中找到这条边界.

    Args:
        lst1 (list[int]): 顺序表1
        lst2 (list[int]): 顺序表2

    Returns:
        float: 中位数.
    """
    m, n = len(lst1), len(lst2)

    def get_Kth_element(k):
        idx1, idx2 = 0, 0
        while True:
            if idx1 == m:
                return lst2[idx1 + k - 1]
            if idx2 == n:
                return lst1[idx1 + k - 1]
            if k == 1:
                return min(lst1[idx1], lst2[idx2])

            new_idx1 = min(idx1 + k // 2 - 1, m - 1)
            new_idx2 = min(idx2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = lst1[new_idx1], lst2[new_idx2]
            if pivot1 <= pivot2:
                k -= new_idx1 - idx1 + 1
                idx1 = new_idx1 - 1
            else:
                k -= new_idx2 - idx2 + 1
                idx2 = new_idx2 + 1

    total_length = m + n
    if total_length % 2 == 1:
        return get_Kth_element((total_length + 1) // 2)
    return (
        get_Kth_element(total_length // 2)
        + get_Kth_element(total_length // 2 + 1)
    ) / 2


# END
# TEST
if __name__ == "__main__":
    l1 = [1, 5, 11, 25, 31, 34, 43, 46, 67, 123, 345, 412, 423, 567, 678, 981]
    l2 = [2, 6, 7, 12, 34, 45, 78, 123, 124, 234, 323, 345, 456, 568, 568, 789]
    print(two_order_list_median(l1, l2))
