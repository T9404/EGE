# 1) Решение

f = open('C:\\Users\\XiaoMai\\Downloads\\27-19b.txt')
n = int(f.readline())


s = [1]
max_pr = 0

for i in range(n):
    x = int(f.readline())
    s = [a*x for a in s]+[x]

    for a in s:
        if (a == 0):
            s.remove(0)
        max_pr = max(max_pr, a)

print(max_pr)




# 2) Решение

f = open('27-19b.txt')
n = int(f.readline())


mak, suma = 1, 1

for _ in range(n):
    x = int(f.readline())

    if x != 0:
        suma *= x
    else:
        mak = max(suma, mak)
        suma = 1

print(mak)
