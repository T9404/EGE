'''
Рассмотрим произвольное натуральное число, представим его всеми возможными 
способами в виде произведения двух натуральных чисел и найдём для каждого 
такого произведения разность сомножителей, каждый из которых больше единицы. 
Например, для числа 24 получим: 24 = 2*12 = 3*8 = 4*6, множество разностей 
содержит числа 10, 5 и 2.
Найдите числа в диапазоне [543210; 987654], для которых:

- есть как минимум две различных пары натуральных сомножителей,
- максимальная разность сомножителей кратна минимальной разности сомножителей, 
не равной нулю;
- минимальная разность сомножителей больше 4444.

Для каждого найденного числа выведите два числа: найденное число и минимальную 
разность сомножителей, не равную нулю.
'''
# https://prnt.sc/pK1BjYHn5nWl


def F(n):
    dividers = set()

    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0):
            dividers.add(abs(i - (n // i)))

    if (len(dividers) >= 2) and (min(list(dividers)) > 4444) and (max(list(dividers)) % min(list(dividers)) == 0):
        return min(x for x in dividers if (x != 0))
    else:
        return 0


for i in range(543210, 987655):
    if (F(i) != 0):
        print(i, F(i))
