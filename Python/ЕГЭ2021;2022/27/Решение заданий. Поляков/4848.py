f = open('27-93.txt')
n, k = map(int, f.readline().split())


def func(x):
    if abs(x) % 10 == 3 and x < 0:
        return 1
    return 0


ans = float('-inf')
s = [[0, 0]]


for _ in range(n):
    x = int(f.readline())

    cmb = [[a + x, b + func(x)] for a, b in s] + [[x, func(x)]]

    s = {x[1]: x for x in sorted(cmb) if (x[1] <= k)}

    if k in s:
        s1, k1 = s[k]
        ans = max(ans, s1)

    s = s.values()


print(ans)
