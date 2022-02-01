f = open('26-64.txt')
n, s = map(int, f.readline().split())
''' Вся логика- взяли товары в сумку, которые можем. Поменяли самые дорогие на самые дешевые, не вошедшие в сумку, посчитали '''

def read(n): #чтение данных
    d = []
    for _ in range(n):
        a, b = f.readline().split()
        a = int(a)
        d.append([a, b]) #считывание числа и буквы в массив
    d.sort(key=lambda x: x[0])  #сортировка по возрастанию (по числу-первому элементу)
    return d

def bug_money(d): #добавляем в нашу сумку максимум товаров, пока у нас есть $
    global s
    prom = []
    for m in d:
        if s - m[0] >= 0:
            s -= m[0]
            prom.append(m) 
    prom.sort(key=lambda x: x[0], reverse=True)
    return prom

def find_b(d): #найти 'B'
    j = 0
    while True:
            if d[j][1] == 'B':
                number, word = d[j]
                del(d[j]) #выбрасываем использованное 
                return number, word;
            else:
                j+=1
    return None

def permutations(prom, d): #переставляем элементы так, чтобы кол-во 'B' было наибольшим
    global s
    i = 0
    while True:
        try:
            if prom[i][1] != 'B':
                num, wor = find_b(d)
                if s - num + prom[i][0] >= 0:
                    s = s - num + prom[i][0]
                    prom[i] = num, wor
            i+=1
        except:
            break
    return prom

def count_B(new_prom): #счётчик для ответа
    k = 0
    for m in new_prom:
        if m[1] == 'B':
            k+=1
    return k



d = read(n) #запись в массив
prom = bug_money(d) #добавление любых элементов пока не кончились $
d = d[len(prom):] #зачем нам одинаковые элементы? 
new_prom = permutations(prom, d) #добавление в нашу сумку макс кол-во 'B'
k = count_B(new_prom) #подсчёт 'B'

print(k, s)
