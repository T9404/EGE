# Имеется набор данных, состоящий из троек положительных целых чисел.
# Необходимо выбрать из каждой тройки два числа так, чтобы сумма былла нечетна.
# Найдите максимальную сумму (при которой длина тоже максимальная) подряд идущих нечетных сумм пар в последовательности.
# Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число – максимально возможную длину, соответствующую условиям задачи.

# 1)Авторский способ

from itertools import *


f = open('27-B.txt')
n = int(f.readline())


posl = []

for _ in range(n):
    a = [int(x) for x in f.readline().split()]
    pair = [a[0]+a[1], a[0]+a[2], a[1]+a[2]]
    max_sum = 0

    for i in pair:
        if (i % 2 == 1):
            max_sum = max(max_sum, i)

    posl.append(max_sum)


posl.append(0)
sum, len, max_sum, max_len = 0, 0, 0, 0

for i in posl:
    if (i != 0):
        sum += i
        len += 1
    else:
        if (sum > max_sum) and (sum == max_sum or sum > max_sum):
            max_sum = sum
            max_len = len
        len = 0
        sum = 0

print(max_len)





# 2) Способ от зрителя

from itertools import *


f = open('27-B.txt')
n = int(f.readline())


max_s, max_l = 0, 0
s, l = 0, 0

for _ in range(n):
    para = [int(x) for x in f.readline().split()]
    s1 = sorted([a + b for a, b in combinations(para, 2)])

    m = 0
    for i in s1:
        if i % 2 != 0:
            m = max(m, i)

    if m != 0:
        s += m
        l += 1

    else:
        if (max_l < l) and (s == max_s or s > max_s):
            max_l = l
            max_s = s

        l, s = 0, 0

print(max_l)
