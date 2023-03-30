#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    contests.sort(reverse=True)
    k_reached = False
    res = 0
    k_cnt = 0
    if k == 0:
        k_reached = True
    for i in contests:
        if i[1] == 1:
            if k_reached == False:
                res += i[0]
                k_cnt += 1
                if k_cnt == k:
                    k_reached = True
            else:
                res -= i[0]
        else:
            res += i[0]
    print(res)
    return res
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
