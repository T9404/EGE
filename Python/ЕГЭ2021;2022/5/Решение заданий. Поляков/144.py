"""
(№ 144) Автомат получает на вход пятизначное число. 
По этому числу строится новое число по следующим правилам.
1. Складываются отдельно первая, третья и пятая цифры, 
а также вторая и четвёртая цифры.
2. Полученные два числа записываются друг за другом в порядке 
неубывания без разделителей.
Пример. Исходное число: 63 179. Суммы: 6 + 1 + 9 = 16; 3 + 7 = 10. 
Результат: 1016. Укажите наименьшее число, при обработке которого 
автомат выдаёт результат 621.    
"""
# https://prnt.sc/920WPUe_-Ugg


min_num = float('inf')


for number in range(10000, 100000):
    t = number
    parts_num = []

    while t:
        parts_num.append(t % 10)
        t = t//10
    parts_num = parts_num[::-1]

    result_1 = parts_num[0]+parts_num[2]+parts_num[4]
    result_2 = parts_num[1]+parts_num[3]

    summ = str(min(result_1, result_2))+str(max(result_1, result_2))
    if (summ == '621'):
        min_num = min(min_num, number)


print(min_num)
