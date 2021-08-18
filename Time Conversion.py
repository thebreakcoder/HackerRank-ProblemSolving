# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:49:26 2020

@author: lenovo
"""

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour24 = ""
    hour = ""
    hour += str(s[0])
    hour += str(s[1])
    if "PM" in s and int(hour) < 12:
        if int(s[0]) == 0:  
            hour24 += str(int(s[1]) + 12)
        else:
            hour24 += str(int(s[0]) + 1)
            hour24 += str(int(s[1]) + 2)    
        hour24 += s[2:-2]
    elif "AM" in s and int(hour) == 12:
        hour24 += "00"
        hour24 += s[2:-2] 
    else:
        hour24 += s[0:-2]
    
    return hour24    
        
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
