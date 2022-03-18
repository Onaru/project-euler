from math import sqrt
from re import I

def isPrim(n):
    result = True
    sqrtN = sqrt(n)
    i = 2
    while i <= sqrtN:
        if 0 == n%i:
            result = False
            break
        i += 1
    return result

def primSum(n):
    ps = 0
    i = 2
    while i <= n:
        if isPrim(i):
            ps += i
        i +=1
    return ps

print(primSum(2000000))