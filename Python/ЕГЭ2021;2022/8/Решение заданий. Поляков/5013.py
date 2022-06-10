'''
У Ильи есть набор кубиков, выкрашенный во все семь цветов радуги. В наборе сорок 
два кубика, по 6 штук каждого цвета. Илья строит башенки, ставя кубики один на 
другой в один столбик так, чтобы соседние кубики были разного цвета. Сколько различных 
башенок высотой от 3 до 9 кубиков он может построить?
'''
# https://prnt.sc/-6FYWUE9AT3L


from itertools import product


def check(num):
    arr = list(num)

    for i in range(len(arr)-1):
        if arr[i+1] == arr[i]:
            return False
    return True


count = 0


for r in range(3, 9+1):
    for i in product('0123456', repeat=r):
        number = ''.join(i)
        if check(number):
            count += 1


print(count)
