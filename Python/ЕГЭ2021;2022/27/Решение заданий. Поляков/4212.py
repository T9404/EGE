f = open('27b.txt')
N = int(f.readline())


k = {x: (10**30, 0) for x in range(69)}

s, m, l = 0, 0, 0


for i in range(N):
    x = int(f.readline())
    s += x

    if s - k[s % 69][0] > m or (s - k[s % 69][0] == m and
                                i + 1 - k[s % 69][1] < l):
        m = s - k[s % 69][0]
        l = i + 1 - k[s % 69][1]

    if s < k[s % 69][0]:
        k[s % 69] = (s, i + 1)


print(l)
