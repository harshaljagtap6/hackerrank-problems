#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    posint = 0
    zeroint = 0
    negint = 0
    
    for i in arr:
        if i > 0 :
            posint += 1
        elif i == 0:
            zeroint += 1
        else:
            negint += 1
            
            
    print(format(posint/len(arr), '.6f'));
    print(format(negint/len(arr), '.6f'));
    print(format(zeroint/len(arr), '.6f'));
  
# Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
