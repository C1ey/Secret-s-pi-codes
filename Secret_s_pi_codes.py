#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findSecrets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY queries
#

def find_s(arr):
    n=len(arr)
    for i in arr:
        for j in range(i, n+1):
            pass
    



def findSecrets(arr, queries):
    # Write your code here
    n=len(arr)
    result=1
    if queries <1 or queries>10**5:
        return "Invald Number of Queries"
    if n<2 or n>10^5:
        return "Invalid amount of values for arr"
    for i in arr:
        result *=arr[i]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    results = findSecrets(arr, queries)

    fptr.write('\n'.join(map(str, results)))
    fptr.write('\n')

    fptr.close()
