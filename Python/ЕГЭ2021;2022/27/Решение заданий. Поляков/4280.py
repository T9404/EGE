# 1) Способ

f = open('C:\\Users\\XiaoMai\\Downloads\\27-74b.txt')
n = int(f.readline())


mas = [[0, 0]]
count = 0

for _ in range(n):
    x = int(f.readline())

    mas = [[x+b, c+1] for b, c in mas]+[[x, 1]]
    num = -1

    for i in mas:
        num += 1

        if (i[0] % 39 == 0) and (i[1] <= 20):
            count += 1
        if (i[1] > 20):
            mas.remove(i)

print(count)




# 2) Способ

f = open('27-74b.txt')
n = int(f.readline())


s = [[0, 0]]
k = 0

for i in range(n):
    x = int(f.readline())

    cmb = [[sm + x, c + 1] for sm, c in s] + [[x, 1]]

    j = 0

    while j < len(cmb):
        if cmb[j][0] % 39 == 0 and cmb[j][1] <= 20:
            k += 1

        if cmb[j][1] > 20:
            del(cmb[j])
            j -= 1

        j += 1

    s = cmb
    
print(k)
