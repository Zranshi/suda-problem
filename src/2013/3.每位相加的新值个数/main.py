# -*- coding:utf-8 -*-
# @Time     : 2021/7/27 10:11
# @Author   : Ranshi
# @File     : main.py

# START
def get_number(x: int) -> int:
    res, next_num = 1, sum([int(item) for item in str(x)])
    while x != next_num:
        res += 1
        x = next_num
        next_num = sum([int(item) for item in str(x)])
    return res


# END

# TEST
if __name__ == '__main__':
    print(get_number(11))
