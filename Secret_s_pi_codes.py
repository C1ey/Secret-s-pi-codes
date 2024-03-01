#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'findSecrets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY queries
#


def findSecrets(arr, queries):
    result=[]
    n=len(arr)
    if n<2 or n>10**5:
            return "Invalid Lenght for arr"
    if not isinstance(q, int) and (1<=q<=10**5):
            return "Invalid Values for q"
    for i, j in queries:
        if not isinstance(i, int) and (1<=i<=j):
            return "Invalid Value for i"
        if not isinstance (j, int) and (i<=j<=n):
            return "Invalid Values for j"
        if i==(i+1):
            result.append(i)
        else:
            product=1
            for index in range(i, j+1):
                product *=arr[index-1]
            result.append(product)
    return ([x %((10**9)+7)%((10**9)+7) for x in result])


"""if __name__ == '__main__':
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
"""