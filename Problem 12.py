from math import sqrt

def numOfDiv(n):
    count = 1
    if n%2 != 0:
        count = 0
    else:
        for i in range(1,int(n/2)+1):
            if n%i==0:
                count += 1
    return count

def search(n):
    count = 1
    sumC = 1
    countDiv = 0
    while countDiv < n:
        temp = numOfDiv(sumC)
        if temp > countDiv:
            countDiv = temp
            print(count, sumC, numOfDiv(sumC))
        count += 1
        sumC += count

search(500)
