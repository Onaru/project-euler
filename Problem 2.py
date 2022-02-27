n0 = 1
n1 = 2
temp = 0
sum = 0
while n1 < 4000000:
    temp = n1
    n1 = n1 + n0
    n0 = temp
    if 0 == n0%2:
        sum = sum + n0
print(sum)