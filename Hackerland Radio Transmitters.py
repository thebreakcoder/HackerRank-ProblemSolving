
import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, r):
    x.sort()
    n = len(x)
    count, first_uncovered = 0, 0
    while first_uncovered < n:
        i = first_uncovered
        while i < n and x[i] - x[first_uncovered] <= k:
            i += 1
        while first_uncovered < n and x[first_uncovered] - x[i - 1] <= k:
            first_uncovered += 1
        count += 1
    return count    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
