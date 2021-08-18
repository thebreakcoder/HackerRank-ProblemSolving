import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    countf = 0
    i = 1
    while i != p:
        if i == 1:                 
            if i == p:
               break
            i += 1
            countf += 1
        else:
            if i == n:
                  if i == p:
                    break 
            elif i < n:
                if i == p or i + 1 == p:
                    break  
                i += 2   
                countf += 1
            else:
                 break
    countb = 0
    i = n
    while i != p:
        if i == n:                 
            if i == p:
               break
            if i % 2 == 0:
               countb += 1 
            i -= 1
        else:
            if i == 1:
                  if i == p:
                    break
            elif i % 2 == 0:
                if i == p:
                    break  
                i -= 1   
                countb += 1
            elif i % 2 != 0:
                if i == p or i - 1 == p:
                    break 
                i -= 2                      
                countb += 1
                
    if countf < countb:
        return countf
    else:
        return countb            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()