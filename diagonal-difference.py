#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    lr = 0
    rl = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                print(arr[i][j])
                lr += arr[i][j]
                
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i + j == (len(arr)-1):
                print(arr[i][j])
                rl += arr[i][j]
                
    
                
    return(abs(lr-rl))
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
