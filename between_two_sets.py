#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def gcd(x,y):
    return math.gcd(x,y)
def calc_lcm(x,y):
    return (x*y)//gcd(x,y)



def getTotalX(a, b):
    count_of_int = 0
    act_lcm = reduce(calc_lcm, a)
    gcd_g = reduce(gcd,b)
    for i in range(act_lcm,gcd_g+1,act_lcm):
        if gcd_g%i == 0:
            count_of_int += 1

    print(count_of_int)



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
