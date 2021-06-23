
import math
import os
import random
import re
import sys

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    return -1

def main():
    fptr = open('test.txt', 'r')
    
    t = int(fptr.readline().strip())
    
    for t_itr in range(t):
        n = int(fptr.readline().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, fptr.readline().rstrip().split())))

        m = int(fptr.readline().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, fptr.readline().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        #fptr.write(str(result) + '\n')
        print(result)

    fptr.close()

# Starting point
main()