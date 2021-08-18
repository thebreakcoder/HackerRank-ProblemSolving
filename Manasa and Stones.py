
import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    
    if a > b:
        a , b = b, a
        
    faces = []    
    face = (n - 1) * a
    faces.append(face)
    
    if a == b:
        return faces
    
    for i in range (n - 1):
        face = (face + b) - a
        faces.append(face)
        
    return faces    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()