'''
В чем суть задания? Переписать алгоритм на ЯП. ЯЗЫК ПРОГРАММИРОВАНИЯ.
Конечно, существуют задачи, которые тяжело программируются, например когда не известна начальная строка,
но вы можете подумать и понять, как ее составить
'''


print('>>>>>>>>>')
#3385 К.Ю.Поляков
'''
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, 
в обеих командах v и w обозначают цепочки символов.

1. заменить (v, w) 
2. нашлось (v)

Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет, 
эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось (8887) ИЛИ нашлось (77)
  ЕСЛИ нашлось (8887)
    ТО заменить (8887, 8)
    ИНАЧЕ заменить (77,8)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 120 идущих подряд цифр 7? 
'''
stroka = '7' * 120
#print(stroka)
# ПОКА =>  while
while '8887' in stroka or '77' in stroka:
    if '8887' in stroka:
        stroka = stroka.replace('8887', '8', 1) # 1 -аргумент, в данном случае замена будет один раз при нахождении
    else:
        stroka = stroka.replace('77', '8', 1)
print(stroka)




print('>>>>>>>>>')
#3424 К.Ю.Поляков
'''
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, 
в обеих командах v и w обозначают цепочки символов.

1. заменить (v, w) 
2. нашлось (v)

Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет, 
эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось (63) ИЛИ нашлось (664) ИЛИ нашлось (6665)
  ЕСЛИ нашлось (63) ТО заменить (63, 4) 
  ИНАЧЕ
    ЕСЛИ нашлось (664) ТО заменить (664, 65) 
    ИНАЧЕ
      ЕСЛИ нашлось (6665) ТО заменить (6665, 663) КОНЕЦ ЕСЛИ
    КОНЕЦ ЕСЛИ
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

Какая строка получится в результате применения приведённой выше программы к строке, в которой первая и последняя цифры – 5, 
а между ними стоит 120 цифр 6? В ответе запишите полученную строку. 
'''
word = '5' + '6' * 120 + '5'
#print(word)
while '63' in word or '664' in word or '6665' in word:
    if '63' in word:
        word = word.replace('63', '4', 1)
    elif '664' in word:
        word = word.replace('664', '65', 1)
    elif '6665' in word:
        word = word.replace('6665', '663', 1)

print(word)


print('>>>>>>>')
#3230 К.Ю.Поляков

'''
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов.

1. заменить (v, w) 
2. нашлось (v)

Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет, эта команда не изменяет строку. 
Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось (111)
  заменить (111, 2)
  заменить (2222, 1)
КОНЕЦ ПОКА
КОНЕЦ

Известно, что исходная строка содержала более 80 единиц и не содержала других цифр. Укажите минимально возможную длину исходной строки, 
при которой в результате работы этой программы получится строка, содержащая минимально возможное количество единиц. 
'''
number = 0
min = float('inf')
for i in range(81, 85+1):
    letter = '1' * i

    while '111' in letter:
        letter = letter.replace('111', '2', 1)
        letter = letter.replace('2222', '1', 1)
    #print(letter, i)
    if letter.count('1') < min:
        min = letter.count('1')
        number = i

print(min, number) # P.S. Задача с КОСЯЧНЫМ условием, в ней подразумевается, что "содержащая минимально возможное количество единиц. " 0 единиц входит, хотя по ссути при 0 НЕ СОДЕРЖИТ!!!




print('>>>>>>>>')
#3840 К.Ю.Поляков
'''
Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, 
в обеих командах v и w обозначают цепочки символов.

1. заменить (v, w) 
2. нашлось (v)

Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке нет, эта команда 
не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось(01) ИЛИ нашлось(02) ИЛИ нашлось(03)
  заменить(01, 302)
  заменить(02, 3103)
  заменить(03, 20)
КОНЕЦ ПОКА
КОНЕЦ

Известно, что исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки. После выполнения данной
программы получилась строка, содержащая 30 единиц, 39 двоек и 42 тройки. Сколько двоек было в исходной строке?
'''

#РЕШЕНИЕ
'''
Данная задача не прогается, точнее прогается, но навряд ли вы будете подбирать комбинацию методом брутфорса
Что имеем:
Таблица
01 -> |3|02 -> |331|03 -> |3312|0
02 -> |31|03 -> |312|0
03 -> |2|0

Как решать? Поможет нам математика
Перепишем таблицу:
(x) единиц ---------------> 2x троек, x единиц, x двоек
(y) двоек ------->           y троек, y единиц, y двоек
(z)троек ------------------>    z двоек

Получаем систему: 
стало = было
30 = x + y
39 = x + y + z
42 = 2x + y

Нам нужно найти y

x = (42-y)/2
21 - (y/2)+y=30
y/2=9
y = 18
'''
