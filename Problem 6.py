from re import I


def sumSquare(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i*i
    return sum

def squareSum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    sum = sum*sum
    return sum

print(squareSum(100)-sumSquare(100))
