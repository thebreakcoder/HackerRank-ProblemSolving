
import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    set1 = set(arr)
    set2 = [value + k for value in arr]
    return len(set1.intersection(set2))
    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
