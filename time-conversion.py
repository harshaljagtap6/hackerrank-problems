#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if "AM" in s:
        if int(s[0:2]) == 12:    
            new = int(s[0:2])-12
            print(new)
            converted = s.replace(s[0:2],str(new)*2)
            return(converted[:-2])     
        else:
            return(s[:-2])
    else:
        if int(s[0:2]) == 12:    
            # new = int(s[0:2])-12
            # print(new)
            # converted = s.replace(s[0:2],str(new)*2)
            return(s[:-2]) 
        # print("Its PM boi")
        else:
            new = int(s[0:2])+12
            converted = s.replace(s[0:2],str(new))
            print(converted[:-2])        
            return(converted[:-2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
