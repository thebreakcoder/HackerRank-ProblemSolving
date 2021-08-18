import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count = 0
    number = str(n)
    for i in range (len(number)):
        if int(number[i]) == 0:
            continue
        else:
            if n % int(number[i]) == 0:
               count += 1
    return count              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()