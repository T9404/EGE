'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому 
отрезку [326496; 649632], числа, у которых количество четных делителей равно 
количеству нечетных делителей. При этом в каждой из таких групп делителей не 
менее 70 элементов. Для каждого найденного числа запишите само число и минимальный 
делитель, больший 1000. 
Например, для числа 2018 имеем следующие делители 2 и 1009. Поэтому результатом 
(не принимая во внимание количества делителей) будет пара чисел
2018 1009
'''
# https://prnt.sc/sxHqgZD1L-vU


def func(number):
    dividers = set()

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            dividers.add(i)
            dividers.add(number // i)

    return dividers


for x in range(326496, 649632 + 1):
    array = func(x)
    if array:
        chet = [i for i in array if i % 2 == 0]
        nechet = [i for i in array if i % 2 != 0]

        if (len(chet) == len(nechet)) and (len(chet) > 70):
            answer = [i for i in array if (i > 1000)]
            print(x, min(answer))
