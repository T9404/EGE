# 0 Использование генераторов списков

numbers = [i for i in range(1, 15)]

years = [int('20'+f'{i}'+f'{j}') for i in range(0, 2+1) for j in range(0, 9+1)]

gene = [x if x in 'qw' else '*' for x in 'qwee'] # ['q', 'w', '*', '*']



# 1) Дополнительно
# https://goalkicker.com/PythonBook/



# 2) Системы счисления
# https://ege-study.ru/ru/ege/materialy/informatika/zadacha-16-razbor-razlichnyx-tipov-zadach/



# 3 Нахождение суммы цифр числа
# summa = sum(map(int, str(input())))



# 4 Что такое длина отрезка и количество точек в нем?
# Длина: конец-начало
# Количество: конец-начало+1



# 5 В чем разница между: "=" И "=="

# "==" - сравнение двух объектов
# "=" - присваивание
a = 5
if (a == 5):
    print('ВЕРНО')

       

# 6 Find в python

dring = 'gcGC'
print('gcGC'.find(dring)) # если строка состоит из 'gcGC' то выведет индекс найденного элемента, вывел 0

word = 'gcGCgcGCgcGCgcGCfdsfgcGC'
print('gcGC'.find(word)) #вывел -1, т.к. не нашел элемент 

dr = 'gcGC dased gcGC'
print('gcGC'.find(dr)) # вывел -1, т.к. строка состоит не только из одной комбинации gcGC



# 7 Count в python

string = '88005553535прощепозвонитьчемукого-тозанимать'
print(string.count('0')) # вернет 2, т.к. два нуля в строке. Лучше не играть с этим в 24 задании
print(string.count('5')) # вернет 5



# 8 Проверка на простоту

# I)
if all(1231 % j != 0 for j in range(2, int(1231**0.5)+1)):
    print('Простое')

# II)
def f(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return 'Составное'
    return 'Простое'

print(f(1232))



# 9 Сортировка в питоне

# I)
list_new = [ 2, 213, 41, 414, 1, 1999, 10000, 1, 2, 1]
print(sorted(list_new, key=lambda x: x % 2 ))

# II)
def elem_sort(i):
    return i[1]

a = [['Третий', 3], ['Первый', 1], ['Второй', 3]]
a.sort(key=elem_sort)
print(a) # [['Первый', 1], ['Третий', 3], ['Второй', 3]]

# III)
arr = [sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]  # [[1, 2], [3, 4], [0, 1]]



# 10 Использование yield

# https://all-python.ru/osnovy/yield.html

def number_range(n): # числа Фибоначчи
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a+b
        
data = list(number_range(10000))
print(data[-1])



# 11 Питонический цикл

data = [20, 500, 62, 174]
for i, value in enumerate(data, 1): # мы можем указать начальный индекс (1)
    print(i, value)



# 12 Множества

a = set([1, 1, 2, 2, 3, 3])
print(a) # {1, 2, 3}

a_new = {i for i in [9, 8, 9, 8, 7]}
print(a_new) # {8, 9, 7}



# 13 Работа со словарями:
# Чтобы добавить элемент в словарь нужно указать новый ключ и значение.

sl = {}

sl['abc'] = 12 # abc - ключ, 12 - значение
sl[121] = '121'
sl['rrrr'] = 'mmmm'
sl.pop(121) # можно удалить иначе: del sl[121]

for key, value in sl.items():
    print(key, value) # проходим по словарю



# 14 Filter и Lambda

# I)
d_lis = list(filter(lambda x: x % 2 == 0, [12, 11, 10, 9, 8, 7, 6]))
print(d_lis) # [12, 10, 8, 6]  

# Функция filter применяет функцию ко всем элементам последовательности и возвращает 
# итератор с теми объектами, для которых функция вернула True.
# Мы использовали анонимную функцию lambda

# II)

nums = [10, 111, 102, 213, 314, 515]
up_nums = [n for n in nums if n % 2 == 1]
print(up_nums) # [111, 213, 515]



# 15 Зачем нужен zip?

# zip возвращает итератор с кортежами, в котором n-ый кортеж состоит 
# из n-ых элементов последовательностей, которые были переданы как аргументы

d_key = ['всем привет', 'ты кто']
d_value = ['пока', 'Пихто']
d_dict = dict(zip(d_key, d_value))
print(d_dict) # {'всем привет': 'пока', 'ты кто': 'Пихто'}



# 16 Перевод ИЗ С.С. :  int('число', система счисления)

print(int('1212', 2))
print(int('13741'), 8)



# 17 Использование map

# разделить с помощью пробелов + сделать тип int
num_1, num_2 = map(int, f.readline().split()) 

arr = [1, 2, 3, 4, 5]
new_arr = list(map(lambda x: x + 1 , arr)) # [2, 3, 4, 5, 6]



# 18 Функция sum

array = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2]]
new_array = sum(array, [])
print(new_array) # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]



# 19 Переменные по условию

flag = True if 1 == 1 else False 
print(flag) # True



# 20 Быстрый перевод элементов массива в число

d = [1, 2, 3, 4, 5]
x = int(''.join(map(str, d)))
print(x) # 12345



# 21 Удаление незначащих нулей

# Задача из сайта К.Ю.Полякова

x = (16 ** 44) * (16 ** 30) - ((32**5) * ((8 ** 40) - (8**32)) * ((16 ** 17) - (32 ** 4)))

x_16 = hex(x)[2:]
x_16 = x_16.replace('f', '0') # 00000000000000000000e00000200000100000e00000000000000000000000000000000000
x_16 = x_16.lstrip('0')       # e00000200000100000e00000000000000000000000000000000000



# 22 try - except 

# Используем для поиска ошибок

try: 
    x = 1 / 0 # пытаемся выполнить эту часть
except:
    print("Вы математик") # получаем ошибку и заходим сюда
