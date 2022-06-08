from itertools import product


def sum_del(x):
    a = set()

    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            a.add(i)
            a.add(x//i)

    sumn = sum([i for i in a if i % 2 != 0])
    return sumn


num_1 = [str(i) for i in range(0, 9+1)]

d = ['']
d += num_1
d += [''.join(i) for i in product('0123456789', repeat=2)]
d += [''.join(i) for i in product('0123456789', repeat=3)] # максимум 3, т.к. x < 10^7

arr_217 = []

# нужны наибольшие числа, в начале ставим с символом ? и числом 9 (т.к. стоит левее)
for i in sorted(num_1, reverse=True):
    for j in sorted(d, reverse=True):
        m = int('14'+i+'4'+j)
        if m % 217 == 0:
            arr_217.append(m)
            if len(arr_217) == 7:
                break

    if len(arr_217) == 7:
        break


for i in sorted(arr_217):
    print(i, sum_del(i))
