f = open('27-44b.txt')
n = int(f.readline())


d = [0, 0, 0]  # максимальная и остальные суммы
razn = []  # итоговые 2 разницы


for _ in range(n):

    a = sorted(list(map(int, f.readline().split())),
               reverse=True)  # по убыванию

    for i in range(3):
        d[i] += a[i]  # добавляем к кучкам


    k = []  # массив разностей

    if a[0] % 2 != a[1] % 2:
        k.append(abs(a[0]-a[1]))

    if a[0] % 2 != a[2] % 2:
        k.append(abs(a[0]-a[2]))


     # добавили все разности, дальше проверяем
    if len(k) == 2:
        razn.append(min(k))  # минимальную из 2
    elif len(k) == 1:
        razn.append(k[0])  # просто разницу


    razn.sort()  # сортируем по возрастанию все разницы
    razn = razn[:2]  # удаляем мусор


print(d[0]-sum(razn))
