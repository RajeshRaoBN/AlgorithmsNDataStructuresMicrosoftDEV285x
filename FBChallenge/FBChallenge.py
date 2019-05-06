#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'goodSegment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY badNumbers
#  2. INTEGER l
#  3. INTEGER r
#

def goodSegment(badNumbers, l, r):
    print(range(l,r))
    badNumbers.sort()
    print(badNumbers)
    rng = []
    lenlist = []
    start = l
    for i in badNumbers:
        if i < r:
            rng.append(list(range(start,i)))
            start = i + 1
        else:
            rng.append(list(range(start,r+1)))
            start = i + 1
        print(rng)
    for j in rng:
        lenlist.append(len(j))
    print(lenlist)
    print(max(lenlist))



#if __name__ == '__main__':

badNumbers = [4, 8, 6,20,12]
l = 1
r = 30
goodSegment(badNumbers, l, r)