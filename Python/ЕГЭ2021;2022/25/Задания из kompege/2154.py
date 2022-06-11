'''
Среди чисел, принадлежащих отрезку: [5000000; 10000000], найти такие, которые могут 
являться точками градусных мер π∙n (n - целое число) на окружности (например, точка 
6π соответствует 1080 градусам на окружности), количество делителей которых более 400, 
но менее 440. Вывести эти числа, справа от каждого вывести соответствующий ему 
наибольший простой делитель.
'''
# https://prnt.sc/zw2X5DSLECVd


def prime(x):
    return all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def f(x):
    dividers = set()

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            dividers |= {i, x//i}

    dividers = sorted(dividers)
    prime_dividers = [i for i in dividers if prime(i)]

    if (400 < len(dividers) < 440) and (len(prime_dividers) >= 1):
        return max(prime_dividers)
    return 0


for i in range(5000000, 10000000 + 1):
    if i % 180 == 0 and f(i):
        print(i, f(i))
