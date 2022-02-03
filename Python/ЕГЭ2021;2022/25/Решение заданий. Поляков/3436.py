def F(n):
    a = set()

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)

    a = list(a)
    a.sort()

    return a


def G(n):
    if len(n) < 2:
        return False
        
    for i in range(0, len(n)-1):
        if n[i]+2 != n[i+1]:
            return False
    else:
        return True


for i in range(834567, 1143211):
    if len(F(i)) != 0 and G(F(i)) == True:
        print(i, max(F(i)))
