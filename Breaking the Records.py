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

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    countmin = 0
    countmax = 0
    result = []
    
    for i in range (len(scores)):
        if maximum < scores[i]:
            maximum = scores[i]
            countmax += 1
    for i in range (len(scores)):
        if minimum > scores[i]:
            minimum = scores[i]
            countmin += 1
    result.append(countmax)
    result.append(countmin)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()