'''
Обозначим через F целую часть среднего арифметического всех простых делителей 
целого числа, не считая самого числа. Если таких делителей у числа нет, то считаем 
значение F равным нулю. Напишите программу, которая перебирает целые числа, 
большие 650000, в порядке возрастания и ищет среди них такие, для которых значение F 
при делении на 37 даёт в остатке 23.

Выведите первые 4 найденных числа в порядке возрастания и справа от каждого числа – 
соответствующее значение F.  
Количество строк для записи ответа избыточно.
'''
# https://prnt.sc/OO5Bnu1I9Jz6


def prime(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def condition(n):
    dividers = set()

    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            if (prime(i) == True):
                dividers.add(i)
            if (prime(n//i) == True):
                dividers.add(n//i)

    if (len(dividers) != 0) and ((sum(dividers)//len(dividers)) % 37 == 23):
        return sum(dividers)//len(dividers)
    return 0


count = 0


for i in range(650001, 10000000, 1):
    if condition(i) != 0:
        count += 1

        if (count <= 4):
            print(i, condition(i))
        else:
            break
