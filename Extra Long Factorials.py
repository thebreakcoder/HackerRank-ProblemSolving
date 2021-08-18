import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    factorial = 1;
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
        print(factorial)
   
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)