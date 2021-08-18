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

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
   
    myset = set(arr)
    mylist = []
    mydic = {}
    
    for i in myset:
        count = arr.count(i)
        mydic[i] = count
            
    maximum = 0
    
    for i in mydic:
        if maximum < mydic[i]:
            maximum = mydic[i]
            result = i
    
    for i in mydic:
        if maximum == mydic[i] and result != i:
            result = min(result, i)       
     
    return result        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()