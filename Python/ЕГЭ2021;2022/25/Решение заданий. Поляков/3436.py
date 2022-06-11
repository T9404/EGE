'''
Рассматривается множество целых чисел, принадлежащих числовому отрезку [834567; 1143210]. 
Найдите числа, нетривиальные делители которых образуют арифметическую прогрессию с 
разностью d = 2. В ответе для каждого такого числа (в порядке возрастания) запишите 
сначала само число, а потом – его максимальный нетривиальный делитель.
'''
# https://prnt.sc/A2tyC-T4a6Hn


def find_dividers(n):
    dividers = set()

    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            dividers.add(i)
            dividers.add(n // i)

    return sorted(dividers)


def progression(number):
    if len(number) < 2:
        return False

    for i in range(0, len(number)-1):
        if (number[i]+2 != number[i+1]):
            return False
    else:
        return True


for i in range(834567, 1143211):
    if (len(find_dividers(i)) != 0) and (progression(find_dividers(i)) == True):
        print(i, max(find_dividers(i)))
