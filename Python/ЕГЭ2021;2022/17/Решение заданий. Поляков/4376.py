f = open('17-10.txt')

a = [int(x) for x in f]


k, sumka = 0, 0

for i in range(1, len(a)-1):
    z = sorted([a[i-1], a[i], a[i+1]])
    if ( z[0] ** 2 + z[1] ** 2) == (z[2]**2):
        k+=1
        sumka+= z[2]

print(k, sumka)
