# 1) Способ

f = open('C:\\Users\\XiaoMai\\Downloads\\27-35b.txt')
n = int(f.readline())


a = []

c, c0 = 0, 0

for _ in range(n):
    x = int(f.readline())

    if (x == 0):
        c0 += 1
    else:
        if (c0 > 0):
            for q in a:
                if ((q[1]-c0) != 0) and ((q[0]+x) % 2 == 0):
                    c += 1

        a.append([x, c0])

print(c)


# 2) Способ

f = open('27-35b.txt')
n = int(f.readline())


there_is_zero, without = [0, 0], [0, 0]
ans = 0

for _ in range(n):
    x = int(f.readline())

    if x == 0:
        there_is_zero[0] += without[0]
        there_is_zero[1] += without[1]
        without = [0, 0]
    else:
        ans += there_is_zero[x % 2]
        without[x % 2] += 1

print(ans)
