#!/bin/python3

import math
import os
import random
import re
import sys


def hackerrankInString(s):
    w = list('hackerrank')
    for c in s:
        if c == w[0]:
            w.pop(0)
            if len(w) == 0:
                return 'YES'
    return 'NO'
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()

