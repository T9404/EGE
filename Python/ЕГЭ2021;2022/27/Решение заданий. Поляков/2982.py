sD = lambda x: sum(int(y) for y in str(x))

for t in 'ab':
    with open(f'27-39{t}.txt') as f:
        a = [int(x) for x in f][1:]

        k = [0]*1000
        for x in a:
            k[x] += 1

        s, c = 0, 0
        for j in range(1000):
            if k[j]:
                assima = int(str(j)[::-1])
                if assima != j:
                    if k[assima]:
                        if k[j] <= k[assima]:
                            s += (k[j]*sD(j) + k[j]*sD(assima))
                        else:
                            s += ((sD(j)*k[assima]) + sD(assima)*k[assima])
                else:
                    if k[j]%2:
                        k[j] -= 1
                        c = max(c, j)
                    s += (k[j]*sD(j))
                    
                k[j], k[assima] = 0, 0

        print(s + sD(c))
