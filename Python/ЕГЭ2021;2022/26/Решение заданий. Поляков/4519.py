''' 
Вся логика- взяли товары в сумку, которые можем. Поменяли самые дорогие на самые дешевые, 
не вошедшие в сумку, посчитали 
'''
# https://prnt.sc/HupPcEYlW1Os


f = open('26-64.txt')
n, s = map(int, f.readline().split())


def read(n):  
    arr = []

    for _ in range(n):
        a, b = f.readline().split()
        a = int(a)
        # считывание числа и буквы в массив
        arr.append([a, b])  
    
    # сортировка по возрастанию (по числу-первому элементу)
    arr.sort(key=lambda x: x[0])

    return arr


# добавляем в нашу сумку максимум товаров, пока у нас есть $
def bug_money(arr):  
    global s
    cost = []

    for m in arr:
        if s - m[0] >= 0:
            s -= m[0]
            cost.append(m)

    return cost.sort(key=lambda x: x[0], reverse=True)


# найти 'B'
def find_b(arr):  
    j = 0

    while True:
        if arr[j][1] == 'B':
            number, word = arr[j]
            # выбрасываем использованное
            del(arr[j])  
            return number, word
        else:
            j += 1


# переставляем элементы так, чтобы кол-во 'B' было наибольшим
def permutations(cost, arr):
    global s
    i = 0

    while True:
        try:
            if cost[i][1] != 'B':
                num, wor = find_b(arr)
                if s - num + cost[i][0] >= 0:
                    s = s - num + cost[i][0]
                    cost[i] = num, wor
            i += 1
        except:
            break

    return cost


# счётчик для ответа
def count_B(new_cost):
    k = 0

    for m in new_cost:
        if m[1] == 'B':
            k += 1

    return k



# запись в массив
arr = read(n)  

# добавление любых элементов пока не кончились $
cost = bug_money(arr) 

# зачем нам одинаковые элементы? 
arr = arr[len(cost):]  

# добавление в нашу сумку макс кол-во 'B'
new_cost = permutations(cost, arr)  

# подсчёт 'B'
k = count_B(new_cost)  


print(k, s)
