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

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    result = ""
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            result += "12.09."
        else:
            result += "13.09."
     
    elif year == 1918:
        result += "26.09."
                          
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            result += "12.09."
        else:
            result += "13.09."  
       
    result += str(year)    
            
    return result         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()