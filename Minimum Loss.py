#!/bin/python3

import math
import os
import random
import re
import sys
from copy import *


def minimumLoss(price):
    temp_price = deepcopy(price)  
    sorted_price = sorted(price)
    min_diff = sorted_price[1] - sorted_price[0]
    for i in range(1, len(sorted_price)):
        if sorted_price[i] - sorted_price[i-1] < min_diff and temp_price.index(sorted_price[i]) < temp_price.index(sorted_price[i-1]):
            min_diff = sorted_price[i] - sorted_price[i-1]
    return min_diff        

if __name__ == '__main__':
    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)
    
    print(result)

   

    
    
