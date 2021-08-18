import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    myset = set(ar)
    mylist = []
    pairs = 0
    for element in myset: 
        mylist.append(ar.count(element))
    print(mylist)   
    for i in range (len(mylist)):
        while(mylist[i] >= 2):
            if mylist[i] % 2 == 0:
                pairs += (mylist[i] / 2)
                break
            mylist[i] -= 1         
    return int(pairs)            
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()