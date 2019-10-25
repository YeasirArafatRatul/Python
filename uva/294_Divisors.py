'''
@author: Yeasir Arafat Ratul
'''
import sys
from math import sqrt
from collections import Counter

def primeFact(n):
    i = 2
    while i <= sqrt(n):
        if n%i == 0:
            l = primeFact(n/i)
            l.append(i)
            return l 
        i+=1
    return [n]


if __name__== "__main__":
    
    number = int(input())

    for iterable in range(number):
        L,U = map(int,input().split())
        it = L 
        result = 0
        maximum_I = -1
        
        while it<=U:
            f = primeFact(it)
            counter = Counter(f)
            result1 = 1
            
            for c in counter:
                result1 *= counter[c] + 1
            if result1 > result:
                result = result1
                maximum_I = it 
            it+=1
        if L == 1 and U == 1:  
            print("Between %d and %d, %d has a maximum of 1 divisors."%(L,U,maximum_I))
        else:
            print("Between %d and %d, %d has a maximum of %d divisors."%(L,U,maximum_I,result))

