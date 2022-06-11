'''
Основная волна 2021
Найдите 5 чисел больших 500000, таких, что среди их делителей есть число, 
оканчивающееся на 8, при этом этот делитель не равен 8 и самому числу.
В качестве ответа приведите 5 наименьших чисел, соответствующих условию.
Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке сначала 
выводится само число, затем минимальный делитель, оканчивающийся на 8, 
не равный 8 и самому числу.
'''
# https://prnt.sc/BXOtS0tFxAy8


def find_dev(n):
    dividers = sorted({(i, n//i) for i in range(2, int(n ** 0.5) + 1) if (n % i == 0)})
    result = float('inf')

    for i in dividers:
        if (i[0] % 10 == 8) and (i[0] != 8) and (i != n):
            result = min(result, i[0])

        if (i[1] % 10 == 8) and (i[1] != 8) and (i != n):
            result = min(result, i[1])

    if result != float('inf'):
        return result
    return False


i = 500_000
count = 0


while count < 5:
    i += 1
    if find_dev(i):
        count += 1
        print(i, find_dev(i))
