#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    list_len = len(a)
    cnt = 0
    for i in range(list_len):
        for j in range(list_len-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                cnt += 1
    print("Array is sorted in",cnt,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
    return

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
