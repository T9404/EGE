f = open('27b.txt')
n = int(f.readline())


k_2000 = [0] * (2000 + 1)


for _ in range(n):
    x = int(f.readline())

    if x <= 2000:
        k_2000[x] += 1


ans = k_2000[1000]*(k_2000[1000]-1) // 2

for i in range(1000):
    ans += (k_2000[i]*k_2000[2000-i])

print(ans)
