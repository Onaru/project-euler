from operator import truediv
from pickle import FALSE


i = 1
lpf = 0
n = 600851475143
while i < n:
    if 0 == n%i:
        temp = True
        for j in range(2,i):
            if 0 == i%j:
                temp = False
        if temp == True:
            lpf = i
            print(lpf)
    i+=1
print(lpf)
