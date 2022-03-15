f = open('27b.txt')
a = [int(x) for x in f][1:]


k = [0]*1000
for x in a:
    k[x] += 1


def sD(x): 
    return sum(int(y) for y in str(x))


s, c = 0, 0

for j in range(1000):
    if k[j]:
        assima = int(str(j)[::-1])

        if assima != j and k[assima]:
            if k[j] <= k[assima]:
                s += (k[j]*sD(j) + k[j]*sD(assima))
            else:
                s += ((sD(j)*k[assima]) + sD(assima)*k[assima])

        else:
            if k[j] % 2:
                k[j] -= 1
                c = max(c, j)

            s += (k[j]*sD(j))

        k[j], k[assima] = 0, 0


print(s + sD(c))
