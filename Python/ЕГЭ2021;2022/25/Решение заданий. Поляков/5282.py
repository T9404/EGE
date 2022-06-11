'''
Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» 
может задавать и пустую последовательность.
Найдите 7 наибольших чисел, меньших 107, которые кратны 217 и удовлетворяют маске 14?4*. 
Выведите эти числа в порядке возрастания, справа от каждого числа выведите сумму его нечётных делителей.
'''
# https://prnt.sc/hys_MtZZtEk1


from itertools import product


def sum_dividers(number):
    dividers = set()

    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            dividers.add(i)
            dividers.add(number//i)

    sumn = sum([i for i in dividers if (i % 2 != 0)])
    return sumn


# максимум 3, т.к. number < 10^7
d = ['']
d += [str(i) for i in range(0, 9+1)]
d += [''.join(i) for i in product('0123456789', repeat=2)]
d += [''.join(i) for i in product('0123456789', repeat=3)]

nums_217 = []


# нужны наибольшие числа, в начале ставим с символом ? и числом 9 (т.к. стоит левее)
for i in sorted([str(i) for i in range(0, 9 + 1)], reverse=True):
    for j in sorted(d, reverse=True):
        m = int('14' + i + '4' + j)
        if (m % 217 == 0):
            nums_217.append(m)
            if len(nums_217) == 7:
                break
            
    if len(nums_217) == 7:
        break


for i in sorted(nums_217):
    print(i, sum_dividers(i))
