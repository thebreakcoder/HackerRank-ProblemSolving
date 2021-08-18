
import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    
    gridlist = []
    for i in range (len(grid)):
        gridlist.append(list(grid[i]))
    
    for i in range (len(gridlist)):
        if i == 0 or i == len(gridlist) - 1:
            continue
        for k in range (len(gridlist)):
            if k == 0 or k == len(gridlist) - 1:
                continue
            if gridlist[i][k] > gridlist[i + 1][k] and gridlist[i][k] > gridlist[i - 1][k] and gridlist[i][k] > gridlist[i][k + 1] and gridlist[i][k] > gridlist[i][k - 1]:
                gridlist[i][k] = 'X'     
                
    result = map(''.join, gridlist)
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
