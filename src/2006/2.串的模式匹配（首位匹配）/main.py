# -*- coding:utf-8 -*-
# @Time     : 2021/7/18 21: 21
# @Author   : Ranshi
# @File     : main.py


# START
def index(source: str, target: str) -> int:
    """
    字符串定位操作.
    在字符串中找到目标字符串的起始下标.
    在定位操作过程中, 首先定位目标字符串的首尾, 如果首位字符符合, 再匹配中间字符.

    Args:
        source (str): 源字符串.
        target (str): 目标字符串.

    Returns:
        int: 目标字符串在源字符串的起始下标.
    """
    len_s = len(source)
    len_t = len(target)
    if len_t == 0 or len_s == 0:
        return -1
    for i in range(0, len_s - len_t - 1):
        if source[i] == target[0] and source[i + len_t - 1] == target[-1]:
            if source[i:i + len_t] == target:
                return i
    return -1


# END

# TEST
if __name__ == '__main__':
    print(index('1243124124124', '12412'))
