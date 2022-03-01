n = 0
for i in range(1000):
    if 0 == i%3:
        n = n+i
    elif 0 == i%5:
        n = n+i
print(n)
