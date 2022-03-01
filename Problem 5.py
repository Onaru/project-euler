def search():
    n = 1
    while True:
        maybe = True
        for i in range(2,21):
            if 0 != n%i:
                maybe = False
                break
        if maybe:
            return n
        n += 1

print(search())
