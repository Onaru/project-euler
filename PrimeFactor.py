n = 2
while n < 102:
    temp = True
    for i in range(2,n):
        if 0 == n%i:
            temp = False
    if temp == True:
        print(n)
    n+=1