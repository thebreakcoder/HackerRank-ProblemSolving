import math
import os
import random
import re
import sys


def marsExploration(s):
    return sum(s[i] != "SOS"[i%3] for i in range(len(s)))               

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
