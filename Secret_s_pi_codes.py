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


def findSecrets1(arr, queries):
    result=[]
    n=len(arr)
    for i, j in queries:
        product=1
        for index in range(i, j+1):
            if i==(j+1):
                product.append(i)
            else:
                product *=arr[index]
            result.append(product)
    return result


def findSecrets1(arr, queries):
    result=[]
    n=len(arr)
    for i, j in queries:
        product=1
        for index in range(i, j+1):
            product *=arr[index]
        result.append(product)
    return result



def findSecrets(arr, queries):
    # Write your code here
    n=len(arr)
    q=len(queries)
    result=1
    if q <1 or q>10**5:
        return "Invald Number of Queries"
    if n<2 or n>10**5:
        return "Invalid amount of values for arr"
    for i in queries:
        result *=arr[i]
    return result
pass




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