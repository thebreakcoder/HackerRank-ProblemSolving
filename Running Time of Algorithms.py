#!binpython3

import math
import os
import random
import re
import sys



def runningTime(arr)
    
    count = 0
    
    for i in range(1, len(arr))
        key = arr[i]
        j = i-1
        while j = 0 and key  arr[j] 
                arr[j + 1] = arr[j]
                j -= 1
                count += 1
        arr[j + 1] = key
    return count    

if __name__ == '__main__'

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(runningTime(arr))

    
