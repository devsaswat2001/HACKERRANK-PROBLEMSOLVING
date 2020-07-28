#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    new_arr = sorted(arr)
    max = 0
    min = 0
    for i in range(4):
        min += new_arr[i]
        print(min)
    for j in range(4,0,-1):
        max += new_arr[j]
        print(max)
    print(min, max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
