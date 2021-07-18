# -*- coding:utf-8 -*-
# @Time     : 2021/7/18 17: 20
# @Author   : Ranshi
# @File     : main.py

# START
def permutations(n: list, begin: int = 0, end: int = None):
    if not end:
        end = len(n)
    res = []

    def dfs(arr: list, le: int, ri: int):
        if le >= ri:
            res.append(arr[:])
        else:
            i = le
            for num in range(le, ri):
                arr[num], arr[i] = arr[i], arr[num]
                dfs(arr, le + 1, ri)
                arr[num], arr[i] = arr[i], arr[num]

    dfs(n, begin, end)
    return res


# END

# TEST
if __name__ == '__main__':
    test_arr = [1, 2, 3]
    for i in permutations(test_arr):
        print(i)
