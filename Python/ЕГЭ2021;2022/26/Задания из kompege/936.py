f = open('936.txt')
n, s = map(int, f.readline().split())


values = sorted([int(x) for x in f.readlines()], reverse=True)

k, i = 0, 0

while values:
    ship = []  # новый корабль

    for j in range(len(values)):
        if sum(ship) + values[j] <= s:  # заполняем на максимум
            ship.append(values[j])
            values[j] = None  # уплыло и пропало

    values = [i for i in values if i != None]  # убираем ненужное
    k += 1

print(k, sum(ship))
