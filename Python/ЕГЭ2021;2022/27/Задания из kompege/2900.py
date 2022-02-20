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
