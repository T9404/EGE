f = open('27-96b.txt')
n = int(f.readline())


sums = [float('inf')]*n
defirent = [None]*n

s, k5, k7, ans = 0, 0, 0, float('-inf')


for _ in range(n):
    x = int(f.readline())
    s += x

    if x % 5 == 0:
        k5 += 1
    if x % 7 == 0:
        k7 += 1


    if k5 == k7:
        ans = max(s, ans)

    else:
        if defirent[k5-k7] != None:
            cand = s - sums[k5-k7]
            ans = max(cand, ans)


    if s < sums[k5-k7]:
        sums[k5-k7] = s
        defirent[k5-k7] = k5 - k7


print(ans)