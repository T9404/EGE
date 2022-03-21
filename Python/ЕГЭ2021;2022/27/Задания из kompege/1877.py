f = open('27B.txt')
n = int(f.readline())


l = [float('inf')] * 69
sums = [float('inf')] * 69

max_sum, min_len = 0, float('inf')
s = 0


for i in range(1, n+1):
    x = int(f.readline())
    s += x

    if s % 69 == 0:
        max_sum = s
        min_len = i
    else:

        if l[s % 69] != float('inf'):
            s1 = s - sums[s % 69]
            l1 = i - l[s % 69]

            if s1 > max_sum or (max_sum == s1 and l1 < min_len):
                max_sum = s1
                min_len = l1

    if sums[s % 69] > s:
        sums[s % 69] = s
        l[s % 69] = i


print(min_len)
