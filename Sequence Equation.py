import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p, n):
    mylist = p[0:len(p)]
    p.sort()
    y = []
    for i in range (n):
        y.append(mylist.index(mylist.index(p[i]) + 1) + 1)
    return y   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p, n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()