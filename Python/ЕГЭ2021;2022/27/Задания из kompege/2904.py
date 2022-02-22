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
