# -*- coding:utf-8 -*-
# @Time     : 2021/7/18 21: 21
# @Author   : Ranshi
# @File     : main.py

# START
def index(s: str, t: str) -> int:
    length_s = len(s)
    length_t = len(t)
    if length_t == 0 or length_s == 0:
        return -1
    for i in range(0, length_s - length_t - 1):
        if s[i] == t[0] and s[i + length_t - 1] == t[-1]:
            if s[i:i + length_t] == t:
                return i
    return -1


# END

# TEST
if __name__ == '__main__':
    print(index('1243124124124', '12412'))
