f = open('27B.txt')
n = int(f.readline())


count_g = [0]*11
k_5, ans = 0, 0

for _ in range(n):
    x = int(f.readline())

    if x % 5 == 0:
        k_5 += 1
    if k_5 % 11 == 0:
        ans += 1 

    ans += count_g[k_5 % 11]

    count_g[k_5 % 11] += 1

print(ans)