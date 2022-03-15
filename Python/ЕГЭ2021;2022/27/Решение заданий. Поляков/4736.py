f = open('27b.txt')
N, K = map(int, f.readline().split())


s = {0: 0}
r = (0, 0)


for _ in range(N):
    x = int(f.readline())

    c = [[x + y, 1 + s[y]] for y in s.keys()]

    for sm, ln in c:
        if (sm <= K) and ((sm not in s) or (ln > s[sm])):
            s[sm] = ln


for sm, ln in s.items():
    if (abs(K - sm) < abs(K - r[0])) or ((abs(K - sm) == abs(K - r[0])) and ln > r[1]):
        r = (sm, ln)


print(r[1])
