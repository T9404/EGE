'''
1) Дополнительные фишки питона, которые могут быть полезными
https://pavel-karateev.gitbook.io/intermediate-python/funkcionalnoe-programmirovanie/lambdas

2) Системы СС и о них
https://ege-study.ru/ru/ege/materialy/informatika/zadacha-16-razbor-razlichnyx-tipov-zadach/

'''

#3) Нахождение суммы цифр числа
#summa = sum(map(int, str(input())))

#4) Что такое длина отрезка и количество точек в нем?
#Длина: конец-начало
#Количество: конец-начало+1

#5) В чем разница между ‘is’ и ‘==’ в python

'''
Оператор is сравнивает идентичность двух объектов,
в то время как оператор == сравнивает значения двух объектов.
https://programmera.ru/uroki-po-python/v-chem-raznitsa-mezhdu-is-i-v-python/
'''

list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)
print(list_2)
print(list_3)

print('>>>>> == ')
print(list_1 == list_2)
print(list_1 == list_3)

print('>>>>> is ')
print(list_1 is list_2)
print(list_1 is list_3)
