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

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i in range (len(apples)):
        apples[i] +=  a
    for i in range (len(oranges)):
        oranges[i] += b
    
    count1 = 0
    count2 = 0
    
    for i in range (len(apples)):
        if s <= apples[i] <= t:
            count1 += 1
    for i in range (len(oranges)):
        if s <= oranges[i] <= t:
            count2 += 1        
            
    print(count1)
    print(count2)    
        
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
    fptr.close()