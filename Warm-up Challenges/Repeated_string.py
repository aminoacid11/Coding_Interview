#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    single_cnt = s.count('a')
    if s == 'a':
        return n
    else:
        mult_num = math.floor(n/len(s))
        cnt = single_cnt*mult_num
        mult_word_len = mult_num*len(s)
        remainder = n - mult_word_len
        remaining_str = s[:remainder]
        single_cnt2 = remaining_str.count('a')
        cnt += single_cnt2
        return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
