#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    dict_temp = {}
    for word in magazine:
        dict_temp[word] = dict_temp.get(word,0) + 1
    for word in note:
        if dict_temp.get(word,0) == 0:
            print('No')
            return
        else:
            dict_temp[word] -= 1
    print('Yes')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
