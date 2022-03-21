# 1) Способ

f = open('27B.txt')
n = int(f.readline())


answer, s = 0, 0
max_sum = [10**20]*1000  # Сохраняем минимальные суммы, чтобы при вычитании этих сумм 
                         # получить максимальную сумму(ответ)

for _ in range(n):
    x = int(f.readline())
    s += x

    if (s % 1000 == 0):
        answer = s

    answer = max(answer, s - max_sum[s % 1000])

    max_sum[s % 1000] = min(max_sum[s % 1000], s)


print(answer)

# 2) Способ

f = open('27B.txt')
n = int(f.readline())


s = [0]
ans = 0

for _ in range(n):
    x = int(f.readline())

    cmb = [a + x for a in s] + [x]
    s = {x % 1000: x for x in sorted(cmb)}.values()
    
    for a in s:
        if a % 1000 == 0:
            ans = max(ans, a)

print(ans)
