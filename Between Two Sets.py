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

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    mylist = []
    checked = False
    k = 1
    while k <= b[0]:
        for i in range (len(a)):
             if k % a[i] != 0:
                print(k)
                checked = True
                break
        if checked == False:
            mylist.append(k)
        checked = False    
        k += 1    
    checked = False
    count = 0        
    for i in range (len(mylist)):
        for k in range (len(b)):
            if b[k] % mylist[i] != 0:
                  checked = True
                  break  
        if checked == False:
             count += 1
        checked = False
           
    return count     
                  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()