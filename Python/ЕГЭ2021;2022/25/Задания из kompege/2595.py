'''
Обозначим через P(N) – произведение 5 наименьших различных нетривиальных делителей 
натурального числа N (не считая единицы и самого числа). Если у числа N меньше 5 таких 
делителей, то P(N) считается равным нулю. Найдите 5 наименьших натуральных чисел, 
превышающих 400 000 000, для которых P(N) оканчивается на 17 и не превышает N. 
В ответе для каждого найденного числа запишите сначала значение P(N), а затем – 
наибольший делитель, вошедший в произведение P(N).
'''
# https://prnt.sc/lh69P5s29pw2


def find_dev(n):
    dividers = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dividers.add(i)
            dividers.add(n // i)

    if len(dividers) >= 5:
        a = sorted(dividers)
        return a[0] * a[1] * a[2] * a[3] * a[4], a[4]
    else:
        return 0, 0


i, k = 400_000_000, 0


while k < 5:
    i += 1
    if (find_dev(i)[0] % 100 == 17) and (find_dev(i)[0] < i):
        k += 1
        print(*find_dev(i))
