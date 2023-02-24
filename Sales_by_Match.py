#!/bin/python3
# There is a large pile of socks that must be paired by color. 
#Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    final_cnt = 0
    pass_list = []
    for i in range(n):
        temp_cnt = 1
        temp = ar[i]
        for ind,i2 in enumerate(ar):
            if ind > i and i2 not in pass_list:
                if temp == i2:
                    temp_cnt += 1
                if temp_cnt == 2:
                    final_cnt += 1
                    temp_cnt = 0
        pass_list.append(temp)
    return final_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()