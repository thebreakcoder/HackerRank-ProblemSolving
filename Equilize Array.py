
import math
import os
import random
import re
import sys
from collections import Counter


# Complete the equalizeArray function below.
def equalizeArray(arr):
    occurrences = Counter(arr)
    maximum = occurrences[arr[0]]
    for i in range (len(arr)):
        if maximum < occurrences[arr[i]]:
            maximum = occurrences[arr[i]]
    result = len(arr) - maximum         
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()