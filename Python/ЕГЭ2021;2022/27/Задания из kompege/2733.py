f = open('27B.txt')
n = int(f.readline())


k_80 = [[0, 0] for _ in range(80)]


for _ in range(n):
    x = int(f.readline())

    check = x > 50000
    k_80[x % 80][check] += 1


ans = (k_80[0][1] * (k_80[0][1]-1) // 2 + k_80[40][1] * (k_80[40][1]-1) // 2)
ans += (k_80[0][1] * k_80[0][0] + k_80[40][1] * k_80[40][0])


for i in range(1, 39+1):
    ans += (k_80[i][1]*k_80[80-i][1])

    ans += (k_80[i][1]*k_80[80-i][0])

    ans += (k_80[i][0]*k_80[80-i][1])


print(ans)
