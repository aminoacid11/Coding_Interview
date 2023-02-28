#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    result_arr = []
    for i in range(4):
        for i2 in range(4):
            sum_val = arr[i2][i]+arr[i2][i+1]+arr[i2][i+2]+arr[i2+1][i+1]+arr[i2+2][i]+arr[i2+2][i+1]+arr[i2+2][i+2]
            result_arr.append(sum_val)
    return max(result_arr)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []te

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
