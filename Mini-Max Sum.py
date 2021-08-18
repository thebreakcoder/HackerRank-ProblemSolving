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

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    x = sorted(arr)
    minimumSum = 0
    maximumSum = 0
    result = ""
    for i in range (len(x) - 1):
        minimumSum += x[i]
    for i in range (1, len(x)):
        maximumSum += x[i]
    result += str(minimumSum)
    result += " "
    result += str(maximumSum)
    
    print(result)
            

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
