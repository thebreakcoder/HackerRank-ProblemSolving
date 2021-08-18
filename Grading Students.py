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
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    x = []
    for i in range (len(grades)):
        if int(grades[i]) >= 38:
           grade = int(grades[i]) 
           while grade % 5 != 0:
              grade += 1
           if grade - int(grades[i]) < 3:
               x.append(grade)
           else:
               x.append(grades[i])       
        else:
           x.append(grades[i])  
    
    return x       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()