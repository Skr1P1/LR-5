#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == "__main__":
    def max(*args):
        if args:
            lst = [float(arg) for arg in args]
                
            answ = 1

            for i in lst:
                if lst.index(i) > lst.index(max(lst)):
                    answ *= i
            print(answ)


    print(max(0, 2, 3, 4, 5, 1, 2, -764, 1, 2, 3, 5))
