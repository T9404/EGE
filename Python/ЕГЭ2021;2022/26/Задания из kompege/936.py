'''
Для перевозки партии грузов различной массы выкупают место у компании перевозчиков. 
Компания перевозчик не может принять на борт больше S тонн груза. Известно, 
что отдельный груз нельзя разделить для перевозки, то есть один груз должен доставляться 
одним рейсом на одном грузовом судне. Так же преследуют тактику – перевезти рейсом грузы 
как можно большей массы.
За какое минимальное количество рейсов можно перевезти все грузы?
В ответе запишите два числа – минимальное количество рейсов и суммарную массу грузов, 
которые будут перевезены последним рейсом.
'''
# https://prnt.sc/31kALCK2EHVd


f = open('26.txt')
n, s = map(int, f.readline().split())


values = sorted([int(x) for x in f.readlines()], reverse=True)

count, i = 0, 0


while values:
    # новый корабль
    ship = []

    for j in range(len(values)):
        # заполняем на максимум
        if (sum(ship) + values[j]) <= s:
            ship.append(values[j])
            # уплыло и пропало
            values[j] = None

    # убираем ненужное
    values = [i for i in values if i != None]
    count += 1

print(count, sum(ship))
