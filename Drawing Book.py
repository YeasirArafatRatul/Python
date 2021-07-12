#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    result = 0
    if (n%2==1 and p == n-1) or p == n or n == 2:
        result = 0
        
    elif n%2 == 0 and (p == n-1 or p == n-2):
        result = 1
        
    else:
        if p < n//2 or p == n//2:
            # start from front
            pages = (p-1)/2
            
            if p%2 == 0:
                result = math.ceil(pages)
            else:
                result = math.floor(pages)
         
     
        else:
            # start front back
            pages = (n-p)/2
            result = math.floor(pages)
    
            
    return result

if __name__ == '__main__':


    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
