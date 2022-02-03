f = open('27-73a.txt')
n = int(f.readline())


s1 = [0]*93
sumka = 0

for i in range(n):
    x = int(f.readline())

    s = [0]*93

    for y in range(93):
        if s1[y] != 0:
            a = s1[y] + x
            if a > s[a % 93]:
                s[a % 93] = a

    if x > s[x % 93]:
        s[x % 93] = x

    if s[0] != 0 and s[0] % 2 != 0:
        if sumka < s[0]:
            sumka = s[0]

    s1 = s


print(sumka)
