'''
1) Дополнительные фишки питона, которые могут быть полезными
https://pavel-karateev.gitbook.io/intermediate-python/funkcionalnoe-programmirovanie/lambdas

2) Системы СС и о них
https://ege-study.ru/ru/ege/materialy/informatika/zadacha-16-razbor-razlichnyx-tipov-zadach/

'''

# 3) Нахождение суммы цифр числа
summa = sum(map(int, str(input())))


# 4) Что такое длина отрезка и количество точек в нем?
#Длина: конец-начало
#Количество: конец-начало+1


# 5) Find в python
dring = 'gcGC'
print('gcGC'.find(dring)) #если строка состоит из 'gcGC' то выведет индекс найденного элемента, вывел 0

word = 'gcGCgcGCgcGCgcGCfdsfgcGC'
print('gcGC'.find(word)) #вывел -1, т.к. не нашел элемент 

dr = 'gcGC dased gcGC'
print('gcGC'.find(dr)) # вывел -1, т.к. строка состоит не только из одной комбинации gcGC


# 6) Count в python
string = '88005553535прощепозвонитьчемукого-тозанимать'
print(string.count('0')) #вернет 2, т.к. два нуля в строке. Лучше не играть с этим в 24 задании в подстроках, т.к. теряет. он проходит через строку, а не через элемент
print(string.count('5')) # вернет 5
