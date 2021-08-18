import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    if len(s) == 1:
        print("NO")
        return
    
    length = 1    
    
    while length <= len(s) / 2: 
        first = int(s[:length])
        f = first
        beautiful = ""
        while len(beautiful) < len(s):
           beautiful += str(first)
           first += 1
        if beautiful == s:
          print("YES", f)
          return 
        length += 1                
    
    print("NO")   
     

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        separateNumbers(input())