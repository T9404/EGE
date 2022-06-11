'''
В текстовом файле записан набор натуральных чисел. Гарантируется, что все числа различны. 
Рассматриваются пары с чётной суммой, такие что:
- хотя бы половина чисел набора меньше среднего арифметического пары
- хотя бы четверть чисел набора больше среднего арифметического пары
Определите количество таких пар и наименьшее из средних арифметических таких пар.
'''
# https://prnt.sc/ceWIgbCVEIsO


f = open('26.txt')
n = int(f.readline())


values = sorted([int(x) for x in f.readlines()])

count, answer = 0, float('inf')


for i in range(len(values) - 1):
    for j in range(i + 1, len(values)):
        sumx = (values[i] + values[j])
        if (sumx % 2 == 0):
            sumx //= 2
            if (values[(len(values) // 2) - 1] < sumx) and (values[(len(values)) // 4 * 3] > sumx):
                count += 1
                answer = min(answer, sumx)

print(count, answer)
