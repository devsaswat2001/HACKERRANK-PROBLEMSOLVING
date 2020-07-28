#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    first = 0
    second = 0
    arr_len = len(arr)

    for i in range(arr_len):
        first += arr[i][i]
        print("first:" +str(first))
    i = 0
    j = arr_len - 1
    while (i < arr_len):
        second += arr[i][j]
        print("second: "+str(second))
        i+=1
        j-=1

    print("result: "+str(abs(first - second)))

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)
    result = diagonalDifference(arr)

    #print(result)