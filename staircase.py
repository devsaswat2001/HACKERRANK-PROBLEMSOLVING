#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = 1
    j = n
    while(i<=n):
        print(" "*(j-i)+"#"*i)
        i+=1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
