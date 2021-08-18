
import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    
    topics = []
    i = 0 
    k = i + 1
    
    while True:
        if k == len(topic):
            i += 1
            k = i + 1
        if i == len(topic) - 1:
            break    
        topics.append(str(bin(int(topic[i], 2) | int(topic[k], 2))).count('1'))
        k += 1
             
    result = []
    result.append(max(topics))
    result.append(topics.count(max(topics)))
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
