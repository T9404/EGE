f = open('26-56.txt')
v, k, n = map(int, f.readline().split())


a = [int(x) for x in f]
a.sort(reverse=True)


disk = [0]*k
otl = []

p = ''
for i in range(k):
    p += str(i)


for x in a:
    c = 0

    for i in p:
        i = int(i)
        c += 1

        if (disk[i]+x) <= v:
            disk[i] += x
            p = p[1:len(p)]+p[0]
            break

        elif c == k:
            otl.append(x)


print(sum(otl), len(otl))
