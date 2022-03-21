f = open('27-78b.txt')
n = int(f.readline())


s = [[0, [], 0]]
max_sum = l_min = 0


def gama(z, x):
    z.append(x)
    if len(z) > 2:
        del(z[1])
    return z


for _ in range(n):
    x = int(f.readline())

    cmb = [[a + x, gama(z, x), b + 1] for a, z, b in s] + [[x, [x], 1]]

    s = {sum(x[1]) % 73: x for x in sorted(cmb)}

    if 0 in s:
        a, m, l = s[0]

        if (sum(m) % 73 == 0) and (a % 37 == 0):

            if a > max_sum or (a == max_sum and l < l_min):
                max_sum = a
                l_min = l

    s = s.values()

print(l_min)
