def F(n):
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            return False
    else:
        return True


def G(n):
    a = set()

    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):

            if (F(i) == True):
                a.add(i)
            if (F(n//i) == True):
                a.add(n//i)

    if (len(a) != 0) and ((sum(a)//len(a)) % 37 == 23):
        return sum(a)//len(a)
    else:
        return 0


c = 0

for i in range(650001, 10000000, 1):
    if G(i) != 0:
        c += 1
        
        if (c <= 4):
            print(i, G(i))
        else:
            break
