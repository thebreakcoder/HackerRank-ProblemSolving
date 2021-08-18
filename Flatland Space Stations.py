
import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, m, c):
    c.sort()
    answer = 0
    
    for i in range (1, m):
        answer = max(answer, (c[i] - c[i - 1]) // 2)
    
    answer = max(answer, c[0], n - 1 - (c[-1]))
    
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, m, c)

    fptr.write(str(result) + '\n')

    fptr.close()