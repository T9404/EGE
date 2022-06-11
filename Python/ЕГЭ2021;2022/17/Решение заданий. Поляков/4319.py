'''
В файле 17-4.txt содержится последовательность целых чисел. Элементы последовательности 
могут принимать целые значения от 0 до 10 000 включительно. Рассматривается множество 
элементов последовательности, которые удовлетворяют следующим условиям:
− запись в двоичной системе заканчивается на 1001;
− запись в пятеричной системе заканчивается на 11.
Найдите максимальное из таких чисел и их сумму. Гарантируется, что искомая 
сумма не превосходит 107.
'''
# https://prnt.sc/x8wLR2yILIJT


f = open('17-4.txt')
arr = [int(x) for x in f]


def f(x):
    d = set()

    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)

    d = sorted(d)
    condition = [i for i in d if (i in [2, 3, 5, 7])]

    if len(condition) == 2:
        return 1
    return 0


count, min_elem, max_elem = 0, float('inf'), float('-inf')


for i in range(len(arr)):
    if f(arr[i]) and arr[i] != 0:
        count += 1
        min_elem = min(min_elem, arr[i])
        max_elem = max(max_elem, arr[i])


print(count, min_elem + max_elem)
