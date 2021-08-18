import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    tallest = []
    
    for i in range (len(word)):
        if word[i] == 'a':
           tallest.append(h[0])
        elif word[i] == 'b':
            tallest.append(h[1])
        elif word[i] == 'c':
            tallest.append(h[2])
        elif word[i] == 'd':
            tallest.append(h[3])                 
        elif word[i] == 'e':
            tallest.append(h[4])          
        elif word[i] == 'f':
            tallest.append(h[5]) 
        elif word[i] == 'g':
            tallest.append(h[6]) 
        elif word[i] == 'h':
            tallest.append(h[7]) 
        elif word[i] == 'i':
            tallest.append(h[8]) 
        elif word[i] == 'j':
            tallest.append(h[9]) 
        elif word[i] == 'k':
            tallest.append(h[10]) 
        elif word[i] == 'l':
            tallest.append(h[11]) 
        elif word[i] == 'm':
            tallest.append(h[12]) 
        elif word[i] == 'n':
            tallest.append(h[13]) 
        elif word[i] == 'o':
            tallest.append(h[14]) 
        elif word[i] == 'p':
            tallest.append(h[15]) 
        elif word[i] == 'q':
            tallest.append(h[16]) 
        elif word[i] == 'r':
            tallest.append(h[17]) 
        elif word[i] == 's':
            tallest.append(h[18]) 
        elif word[i] == 't':
            tallest.append(h[19]) 
        elif word[i] == 'u':
            tallest.append(h[20]) 
        elif word[i] == 'v':
            tallest.append(h[21]) 
        elif word[i] == 'w':
            tallest.append(h[22]) 
        elif word[i] == 'x':
            tallest.append(h[23]) 
        elif word[i] == 'y':
            tallest.append(h[24]) 
        else:
            tallest.append(h[25])                 
            
    maximum = max(tallest)
    return maximum * len(word)    
            
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()