#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    flag1 = 0
    result = 0
    for ind,i in enumerate(c):
        if flag1 > 0:
            flag1 -= 1
        else:
            if ind < len(c)-2 and c[ind+2] == 0:
                flag1 = 1
                result += 1
            elif ind < len(c)-1 and c[ind+1] == 0:
                result += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
