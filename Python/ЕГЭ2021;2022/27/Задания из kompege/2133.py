f = open('27_B.txt')
n = int(f.readline())


s = [[[float('inf'), 0] for _ in range(73)] for _ in range(37)]

sum, ma_sum, mi_l = 0, 0, float('inf')
l, fr = 0, 0


for _ in range(n):
    x = int(f.readline())

    if s[sum % 37][x % 73][0] == float('inf'):
        s[sum % 37][x % 73] = [sum, l]

    sum += x
    l += 1

    if l == 1:
        fr = x

    if (sum % 37 == 0) and ((x+fr) % 73 == 0):
        ma_sum, mi_l = sum, l

    s1, l1 = sum-s[sum % 37][(73-x % 73) % 73][0], l - \
        s[sum % 37][(73-x % 73) % 73][1]

    if (s1 > ma_sum) or ((s1 == ma_sum) and (mi_l > l1)):
        ma_sum = s1
        mi_l = l1


print(mi_l)
