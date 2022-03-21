def F(n):
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            return False
    return True


a = [x for x in range(3, 1000001)]
c = []


for i in range(len(a)):
    if (F(a[i]) == False):

        if (len(c) == 0):
            c.append(a[i-1])
        c.append(a[i])

    else:
        c.append(a[i])

        if (len(c)-2 >= 90):
            print(c[0], c[len(c)-1])

        c = []
