#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    
    count = 1
    summation = p
    
    if p > s:
        return 0
     
    if p + (p - d) > s:
        return 1    
    
    while p - d > m:
        p -= d
        print(p)
        summation += p
        if summation > s:
           print("first")
           return count - 1
        if summation == s:
           print("second")
           return count 
        count += 1   
           
    while summation < s:
        summation += m
        print(summation)
        count += 1
        if summation == s:
            print("third")
            return count
        if summation > s:
            print("fourth")
            return count - 1
                        
                 

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
