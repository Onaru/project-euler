from math import sqrt

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

def search(n):
    count = 0
    tempPrim = 1
    while count < n:
        tempPrim += 1
        if isPrim(tempPrim):
            count += 1
    return tempPrim

print(search(10001))