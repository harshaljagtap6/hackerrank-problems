#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alicescore = 0
    bobscore = 0
    score = []
    for alice, bob in zip(a, b):
        if alice > bob:
            alicescore += 1
            # print(alicescore)
        elif alice < bob:
            bobscore += 1
            # print(bobscore)
            
    score.append(alicescore)
    score.append(bobscore)
        
        # print(alice)
        # print(bob)
            
    # for i in alicescore:
    #     score.append(alicescore)        
        
    # for i in bobscore:
    #     score.append(bobscore)      
    return(score)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
