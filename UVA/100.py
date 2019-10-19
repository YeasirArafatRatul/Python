import sys
cache = {}


def function(n):
    if n in cache:
        return cache[n]
    if n == 1:
        return 1
    orgin = n
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n + 1
    count = three(n) + 1
    cache[orgin] = count
    return count

        

if __name__ == '__main__':
    i,j = map(int,input().split())
    if i > j:
        start_point = j
        end_point = i
    else:
        start_point = i
        end_point = j
    maxlength = 0
    
    for n in range(start_point, end_point + 1):
        maxlength = max(maxlength, function(n))
    print(i, j, maxlength)
  
