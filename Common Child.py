
import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    m = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i,c in enumerate(s1,1):
        for j,d in enumerate(s2,1):
            if c == d:
                m[i][j] = m[i-1][j-1]+1
            else:
                m[i][j] = max(m[i][j-1],m[i-1][j])
                   
    return m[-1][-1]

#Time out error with python3. Only works with Pypy3#

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()