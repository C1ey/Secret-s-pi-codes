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
    result = []
    n = len(arr)
    
    if n < 2 or n > 10**5:
        return "Invalid Length for arr"
    
    prefix_products = [1] * (n + 1)
    for i in range(1, n + 1):
        prefix_products[i] = (prefix_products[i - 1] * arr[i - 1]) % (10**9 + 7)
    
    for i, j in queries:
        if not (1 <= i <= j <= n):
            return "Invalid values for i or j"
        
        product = (prefix_products[j] * pow(prefix_products[i - 1], -1, (10**9 + 7))) % (10**9 + 7)
        result.append(product)
    
    return result


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