f = open('27b.txt')
N = int(f.readline())


k = {x: 0 for x in range(71)}

count, s = 0, 0


for i in range(N):
    x = int(f.readline())
    s += x

    count += (k[s % 71] + (s % 71 == 0))

    k[s % 71] += 1


print(count)
