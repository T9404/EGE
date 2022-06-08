from itertools import combinations


f = open('17-328.txt')
a = [int(x) for x in f.readlines()]


# нашли числа -> перевод в строку -> соединим элементы -> найдем сумму цифр строки
summ_22 = sum(map(int, ''.join((str(i) for i in a if i % 22 == 0))))
k, mik = 0, float('inf')


for i in range(len(a)-2):
    # комбинации двух чисел превращаем в сумму (восьмеричная запись)
    summ = [oct(sum(x))[2:]
            for x in list(combinations([a[i], a[i+1], a[i+2]], r=2))]

    # перебор цифр сумм пар чисел через генератор
    if all(t[j] not in '1357' for t in summ for j in range(len(t))):
        if a[i] + a[i+1] + a[i+2] < summ_22:
            k += 1
            mik = min(mik, a[i]+a[i+1]+a[i+2])


print(k, mik)
