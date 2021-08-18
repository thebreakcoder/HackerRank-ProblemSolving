import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    cum = 0
    for i in range (1, n + 1):
        if i == 1:
            cum = 2
            people = 6
        else:
            cum += math.floor(people / 2)
            people = math.floor(people / 2) * 3      
    return cum
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()