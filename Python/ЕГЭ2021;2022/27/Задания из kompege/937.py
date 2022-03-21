f = open('C:\\Users\\XiaoMai\\Downloads\\27-B (9).txt')
n = int(f.readline())


max_s, sr_s, min_s = 0, 0, 0
minr = float('inf')

for _ in range(n):
    c = [int(x) for x in f.readline().split()]
    maxc, src, minc = max(c), sum(c)-max(c)-min(c), min(c)

    max_s += maxc
    sr_s += src
    min_s += minc

    if (src % 2 != minc % 2):

        if (maxc != src):
            minr = min(minr, maxc-src)
        if (maxc != minc):
            minr = min(minr, maxc-minc)


print(max_s-minr)





# P.S. Это не является универсальным решением!
# Нужно каждый раз анализировать полученный файл и смотреть четность чисел в каждой тройке

f = open('27-B (1).txt')
n = int(f.readline())


a = set()
s_1 = s_2 = s_3 = 0

for _ in range(n):
    dmik_1 = float('inf')

    para = sorted([int(x) for x in f.readline().split()])
    s_3 += para[2]
    s_2 += para[1]
    s_1 += para[0]

    if para[2] % 2 != para[1] % 2 or para[0] % 2 != para[2] % 2:

        dmik_1 = min(dmik_1, para[2]-para[1], para[2]-para[0])
        a.add(dmik_1)


b = [i for i in a if i != 0]
b = b[:5]

print(s_3-b[0], s_2, s_1+b[0])
# осталось подвести под условие, т.е. вычесть