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

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range (n - 1):
        for ele in range (i + 1, n):
            if (int(ar[i]) + int(ar[ele])) % k == 0:
                print(i)
                print(ele)
                count += 1
    return count            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()