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

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1 > x2 and v1 > v2:
        return("NO")
    if x1 < x2 and v1 < v2:
        return("NO")
    if v1 == v2:
        return("NO")    
    
    rate1 = v1
    rate2 = v2 
        
    v1 += x1
    v2 += x2 
    
    if x1 < x2:
        while v1 < v2:
          v1 += rate1
          v2 += rate2 
        if v1 == v2:
            return "YES"
        else:
            return "NO"      
        
    if x1 > x2:
        while v1 > v2:
          v1 += rate1
          v2 += rate2 
        if v1 == v2:
            return "YES"
        else:
            return "NO"            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
