#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minStart' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minStart(arr):
    # Write your code here
    flag = 0
    max_neg = 0
    max_pos = 0
    first_pos_flag = False
    for ind,i in enumerate(arr):
        if ind == 0 and i < 0 and arr[1]>=0:
            result = 1-i
            return result
        else:
            if i<0:
                flag = 1
            elif flag == 0 and i > 0:
                max_pos += i
                first_pos_flag = True
            elif flag == 1 and arr[ind+1]<0:
                max_neg += i
            elif flag == 1 and arr[ind+1]>=0:
                max_neg += i
                if first_pos_flag == False:
                    max_pos += arr[ind+1]
                break 
    temp_sum = max_neg + max_pos
    if temp_sum < 1:
        result = 1-temp_sum
    else:
        result = 1
    return result
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minStart(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
