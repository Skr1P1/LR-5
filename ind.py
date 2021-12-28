#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание №14: Найти произведение аргументов, расположенных после максимального по модулю аргумента

import math

def multi(*args):
    list1 = list(args)
    mx = 0
    mul = 1
    maxi = 0
    for a in list1:
        if mx < abs(a):
            mx = abs(a)
            maxi = list1.index(a)
    while len(list1)-1 > maxi:
        mul = mul * list1[maxi+1]
        maxi += 1
    return mul

if __name__ == "__main__":
    print(multi(1, -8, 3, 4, 3))
