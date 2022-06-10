""" 
На вход алгоритма подаётся натуральное число N. Алгоритм строит 
по нему новое число R следующим образом:
1) Строится четверичная запись числа N.
2) К этой записи дописывается ещё три или четыре разряда по следующему 
правилу: если N нечётное, то слева к нему приписывается "2", 
а справа - "11". В противном случае слева приписывается "13", а справа "02".
Например, N = 4510 = 2314 => 2231114 = 277310 = R
Полученная таким образом запись (в ней на три или четыре разряда больше, 
чем в записи исходного числа N) является четверичной записью искомого числа R. 
Укажите наименьшее число R, большее 1000, которое может быть получено с помощью 
описанного алгоритма. В ответ запишите это число в десятичной системе счисления.
"""
# https://prnt.sc/XRCgUicB8pf4


max_numb = float('inf')


for N in range(1, 1000):
    copy_N = N
    N_4 = ''

    while copy_N:
        N_4 += str(copy_N % 4)
        copy_N //= 4

    N_4 = N_4[::-1]
    N_4 = ('2' + N_4 + '11') if (N % 2 == 1) else ('13' + N_4 + '02')

    if (int(N_4, 4) > 1000):
        max_numb = min(max_numb, int(N_4, 4))


print(max_numb)
