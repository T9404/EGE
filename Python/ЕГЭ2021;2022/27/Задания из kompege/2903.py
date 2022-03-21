f = open('27B.txt')
n = int(f.readline())


seq = [0] * n 

k_best, s = 0, 0
ans = float('inf')


for _ in range(n):
    x = int(f.readline())
    s += x 

    if x % 3 == 0:
        k_best += 1

    if k_best == 10:
        ans = min(s, ans)

    if k_best > 10:
        ans = min(ans, s - seq[k_best - 10])
    
    seq[k_best] = max(seq[k_best], s)


print(ans)
