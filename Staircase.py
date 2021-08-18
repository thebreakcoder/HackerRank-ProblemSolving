# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 12:49:26 2020

@author: lenovo
"""

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    result = ""
    for i in range (n):
        for k in range (n):
            if k >= n - (i + 1):
                result += "#"
            else:
                result += " "

        print(result)
        result = ""
if __name__ == '__main__':
    n = int(input())

    staircase(n)