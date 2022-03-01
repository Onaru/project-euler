def testDiv(a,b):
    if 0 == a%b:
        return True
    else:
        return False

def search():
    n = 1
    while True:
        maybe = True
        for i in range(2,21):
            if not testDiv(n,i):
                maybe = False
                break
        if maybe:
            return n
        n += 1

print(search())