#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    n=3
    while 2*n-2<=t:
        n*=2
    return n-(t-(n-2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
