# 1) Способ

f = open('27A.txt')
n = int(f.readline())


sums, l = [-10**20] * 2077, [0]*2077
min_sum, max_len = float('inf'), 0
s = 0


for i in range(1, n+1):
    x = int(f.readline())
    s += x

    if s % 2077 == 0 and s <= min_sum:
        min_sum, max_len == s, i

    else:
        s1 = s - sums[s % 2077]
        l1 = i - l[s % 2077]
        if s1 < min_sum or (min_sum == s1 and l1 > max_len):
            min_sum, max_len = s1, l1

    if s > sums[s % 2077]:
        sums[s % 2077] = s
        l[s % 2077] = i


print(max_len)


# 2) Способ

f = open('27B.txt')
n = int(f.readline())


s = [[0, 0]]
minsum, maxlen = float('inf'), 0


for i in range(1, n+1):
    x = int(f.readline())

    cmb = [ [a+x, b+1] for a, b in s] + [ [x, 1] ]
    s = {x[0]%2077:x for x in sorted(cmb, reverse=True)}.values()

    for a, b in s:
        if (a % 2077 == 0):
            if (a < minsum) or (a == minsum and b > maxlen):
                minsum = a
                maxlen = b
    
print(maxlen)
