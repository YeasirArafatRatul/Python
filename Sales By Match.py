#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pair = 0
    
    for i in range(0,len(ar)):
        first_part_of_pair = ar[i]

        
        for j in range(i+1, len(ar)):
            
            if first_part_of_pair == None:
                continue
            
            if first_part_of_pair == ar[j]:
    
                pair += 1 
                ar[j]= None
                break
             
                
    return pair
        
        

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

