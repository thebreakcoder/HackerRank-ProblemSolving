#!/bin/python3

import math
import os
import random
import re
import sys

def check(i, j, visited,n,m, matrix):
    return(i>=0 and i<n
    and j>=0 and j<m and
    not visited[i][j] and matrix[i][j])
        

def dfs(i,j,visited,n,m, matrix,c):
    
    rows = [-1, -1, -1, 0, 0, 1, 1, 1 ]
    cols = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited[i][j] = True

    for k in range(8):
        if check(i+rows[k], j+cols[k], visited,n,m,matrix):
            c[0]+=1
            dfs(i+rows[k], j+cols[k], visited,n,m,matrix,c)
    

def connectedCell(matrix,n,m):
    
    visited= [[False for j in range(m)] for i in range(n)]
    g = -999

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and matrix[i][j]==1:
                c=[1]
                dfs(i,j,visited,n,m,matrix,c)
                g = max(g,c[0])
    return g



if __name__ == '__main__':

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))
        
    result = connectedCell(matrix,n,m)
    
    print(result)
