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

# Complete the plusMinus function below.
def plusMinus(arr):
    size = len(arr)
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range (size):
        if arr[i] > 0:
            count1 += 1
        elif arr[i] < 0:
            count2 += 1
        else:
            count3 += 1        
    print(count1/size)
    print(count2/size)
    print(count3/size)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)