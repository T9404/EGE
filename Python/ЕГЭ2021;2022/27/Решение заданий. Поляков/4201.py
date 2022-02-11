f = open('файлик')  
n = int(f.readline()) 


s3, s17 = [0], [0]

for _ in range(n):
    groap = [int(x) for x in f.readline().split()]

    para = [groap[0]+groap[1], groap[0]+groap[2],
            groap[1]+groap[2]]  # комбинируем пары

    # комбинации всех пар с предыдущими числами для 3
    cmb3 = [a+b for a in s3 for b in para]

    # комбинации всех пар с предыдущими числами для 17
    cmb17 = [a+b for a in s17 for b in para]


    # из сортированного массива в порядке убывания грузим каждый раз меньшее число с разными остатками и отрезаем знач остатка (для 3, 17)
    s3 = {x % 3: x for x in sorted(cmb3, reverse=True)}.values()

    s17 = {x % 17: x for x in sorted(
        cmb17, reverse=True)}.values()  


mins3 = [x for x in s3 if ((x % 3 == 0) and (x % 17 != 0)) or (
    (x % 3 == 0) and (x % 17 != 0))]  # находим значения, подходящие под условие для деления на  3

mins17 = [x for x in s17 if ((x % 3 == 0) and (x % 17 != 0)) or (
    (x % 3 == 0) and (x % 17 != 0))]  # находим значения, подходящие под условие для деления на  17


print(min(mins3+mins17))  # складываем два массива и находим минимум
