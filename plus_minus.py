#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arr_len = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i < 0:
            neg += 1
        elif i> 0:
            pos+=1
        else:
            zero +=1

    pos_result = pos/arr_len
    neg_result = neg / arr_len
    zero_result = zero / arr_len

    print('%.6f'%pos_result)
    print('%.6f' % neg_result)
    print('%.6f' % zero_result)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
