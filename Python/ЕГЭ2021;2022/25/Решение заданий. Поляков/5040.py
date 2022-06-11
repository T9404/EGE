'''
Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
- символ «?» означает ровно одну произвольную цифру;
- символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может 
задавать и пустую последовательность.
Среди натуральных чисел, не превышающих 109, найдите все числа, соответствующие маске 3?458*3, 
у которых в девятеричной записи цифры идут в порядке невозрастания. В ответе запишите в первом 
столбце таблицы все найденные числа в порядке возрастания, а во втором столбце — суммы цифр их 
девятеричной записи.
'''
# https://prnt.sc/mHMrbTBMDPqs


from itertools import product


def numb_system_9(num):
    numb_9 = []

    while num:
        numb_9.append(num % 9)
        num //= 9

    return (''.join(map(str, numb_9[::-1])))


def sys_numb(num):
    numb_9 = numb_system_9(num)

    for i in range(len(numb_9) - 1):
        if numb_9[i] < numb_9[i+1]:
            return False

    return num, sum(map(int, numb_9))


parts = set()


for i, j, m, n in product('0123456789 ', repeat=4):
    num = int(('3' + i + '458' + j + m + n + '3').replace(' ', ''))
    if num <= 10**9 and sys_numb(num):
        parts.add(sys_numb(num))


for i in sorted(parts, key=lambda d: d[0]):
    print(*i)
