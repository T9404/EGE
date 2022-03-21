f = open('27B.txt')
n = int(f.readline())


k_69 = [0] * 69


for _ in range(n):
    x = int(f.readline())
    k_69[x % 69] += 1


ans = 0

for i in range(len(k_69)):
    ans += (k_69[i] * (k_69[i]-1) // 2)

print(ans)
