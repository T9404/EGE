# 1 Решение

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









# 2 Решение

f = open('27B.txt')
n = int(f.readline())


count_all = [0] * 80
count_big = [0] * 80  # большие 50к
answer = 0

for i in range(n):
    x = int(f.readline())

    ostat = 0 if (x % 80 == 0) else (80 - (x % 80))

    if x > 50000:
        answer += count_all[ostat]
        count_big[x % 80] += 1
    else:
        answer += count_big[ostat]

    count_all[x % 80] += 1


print(answer)
