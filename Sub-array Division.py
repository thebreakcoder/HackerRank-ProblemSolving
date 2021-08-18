# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:49:26 2020

@author: lenovo
"""

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    result = 0
    ways = 0
    i = 0
    v = m
    while i <= len(s) - 1:
        m = v
        result = 0
        k = i
        while m != 0 and k != len(s):
            result += s[k]
            print(s[k])
            k += 1
            m -= 1
        if result == d:
            ways += 1
        i += 1    
            
    return ways
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()