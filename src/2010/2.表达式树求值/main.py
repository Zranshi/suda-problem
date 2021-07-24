# -*- coding:utf-8 -*-
# @Time     : 2021/7/24 10: 52
# @Author   : Ranshi
# @File     : main.py

from src.define import ExpressionTree


# START
def calculate(t: ExpressionTree) -> int:
    if not t.left and not t.right:
        return t.val
    return eval(f'{calculate(t.left)}{t.val}{calculate(t.right)}')


# END

# TEST
if __name__ == '__main__':
    et = ExpressionTree.init_str('+-*15-7    89  ')
    print(calculate(et))
