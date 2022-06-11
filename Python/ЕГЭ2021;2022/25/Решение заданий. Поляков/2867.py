'''
Собственными делители числа – это все его положительные делители, отличные от 
самого́ числа. Число называется полусовершенным, если сумма всех или некоторых 
его собственных делителей совпадает с самим этим числом. Определите количество 
таких чисел в диапазоне [300; 350] и наибольшее из них.
'''
# https://prnt.sc/N9it9P_-Rubf


from itertools import *


count_n, max_number = 0, 0


for numb in range(300, 351):
    dividers = {1}
    amount = 0

    for i in range(2, int(numb ** 0.5) + 1):
        if (numb % i == 0):
            dividers.add(i)
            dividers.add(numb // i)

    if (sum(dividers) >= numb):
        for k in range(2, len(dividers) - 1):
            for q in combinations(dividers, r=k):
                if (sum(dividers) - sum(q) == numb):
                    amount += 1

    if (amount > 0):
        count_n += 1
        max_number = max(max_number, numb)


print(count_n, max_number)
