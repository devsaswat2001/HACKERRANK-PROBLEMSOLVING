#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    # Write your code here.
    num =0
    for i in ar:
        num+=i
    return num


if __name__ == '__main__':


    ar_count = int(input("Array size:"))

    ar = list(map(int, input("spaced integers:").split()))
    print(ar)
    result = simpleArraySum(ar)
    print("result : "+ str(result))


