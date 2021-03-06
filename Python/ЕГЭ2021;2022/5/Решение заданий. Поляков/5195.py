""" 
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему 
новое число R следующим образом.
1) Строится двоичная запись числа N.
2) К полученной записи дописываются разряды. Если в числе четное количество 
единиц, слева дописывается 1 и справа два нуля, если нечетное – слева 
дописываются две единицы.
3) Результат переводится в десятичную систему и выводится на экран.
Пример. Дано число N = 13. Алгоритм работает следующим образом:
1. Двоичная запись числа N: 1101.
2.Число единиц нечетное, следовательно слева дописываем две единицы слева – 
11 + 1101 = 111101.
3. На экран выводится число 61 = 1111012.
Для какого наименьшего значения N результат работы автомата – число, не меньшее 412?
"""
# https://prnt.sc/_eidGiDlGoFt


def f(n):
    n_2 = bin(n)[2:]
    n_2 = ('1' + n_2 + '00') if (n_2.count('1') % 2 == 0) else ('11' + n_2)

    return int(n_2, 2)


for i in range(1, 10000):
    if f(i) >= 412:
        print(i)
        break
