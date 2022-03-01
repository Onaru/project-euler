from curses.ascii import NUL


def palindrome(n):
    s = str(n)
    l = len(s)
    pal = True
    for i in range(round(l/2)):
        if s[i] != s[l-i-1]:
            pal = False
    return pal

def project4():
    temp = 0
    for i in range(100,1000):
        for j in range(100,1000):
            mult = i * j
            if(palindrome(mult) and mult > temp):
                temp = mult
    print(temp)

project4()
