'''
Данное задание не требует пониманий рекурсии. НО! Вы программист? Вам лень?
Рекурсия - это фундамент, через который стоит пройти. Тем более все очень просто

Что посмотреть?
https://www.youtube.com/watch?v=NOaSY5pJmyc&ab_channel=%D0%A2%D0%B8%D0%BC%D0%BE%D1%84%D0%B5%D0%B9%D0%A5%D0%B8%D1%80%D1%8C%D1%8F%D0%BD%D0%BE%D0%B2
'''


print('>>>>>')
#К.Ю.Поляков 3109
'''
Алгоритм вычисления значения функции F(n), где n – натуральное число,
задан следующими соотношениями:

F(n) = 3 при n = 1
F(n) = 2·F(n–1) – n + 1, если n > 1

Чему равно значение функции F(21)?
'''

def f(n):
    if n == 1:
        return 3
    elif n > 1:
        return 2 * f(n-1) - n + 1
print(f(21))



print('>>>>>>>')
#К.Ю.Поляков 2289
'''
Алгоритм вычисления значения функции F(n), где n – натуральное число,
задан следующими соотношениями:

F(n) = n*n + 11, при n ≤ 15
F(n) = F(n//2) + n*n*n - 5*n, при чётных n > 15
F(n) = F(n-1) + 2*n + 3, при нечётных n > 15

Здесь // обозначает деление нацело. Определите количество натуральных
значений n из отрезка [1; 1000],
для которых значение F(n) содержит не менее трёх цифр 6. 
'''

def func(n):
    if n <= 15:
        return n*n+11
    elif n > 15 and n % 2 == 0:
        return func(n//2)+ n**3 - 5*n
    elif n > 15 and n % 2 != 0:
        return func(n-1) + 2 * n + 3

count = 0
for x in range(1, 1000+1):
    number = func(x)
    if str(number).count('6') >= 3: #привет 12 задание.
        count+=1 
print(count) # Берите все фишки языка на заметку и используйте





print('>>>>>>>')
#3132 К.Ю.Поляков
'''
Определите, сколько символов * выведет эта процедура при вызове F(140):

https://prnt.sc/1ar02t6

'''

def F(N):
    global amount
    amount+=1
    if N >= 1:
        amount+=1
        F(N-1)
        F(N//2)
amount = 0
print(F(140)) #None, все логично
print(amount)






 
print('>>>>>') #переделай
#4189 К.Ю.Поляков
'''
Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число,
задан следующими соотношениями:

F(0) = 2
F(n) = F(n–1), при 0 < n ≤ 15
F(n) = 1,6*F(n–3), при 15 < n < 95
F(n) = 3,3*F(n–2), при n ≥ 95

Какая цифра встречается чаще всего в целой части значения функции F(33)? 
'''

def vol(n):
    if n == 0:
        return 2
    elif 0 < n <= 15:
        return vol(n-1)
    elif 15 < n < 95:
        return  1.6 * vol(n-3)
    elif n >= 95:
        return 3.3*vol(n-2)
print(vol(33))
print('Oтвет: 3')









