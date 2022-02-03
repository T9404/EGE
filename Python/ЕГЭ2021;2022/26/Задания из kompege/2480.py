f = open('2480.txt')
n = int(f.readline())


road = [0]*2_000_001  # из условия меньше 2_000_000

for i in range(n):
    a, b = map(int, f.readline().split())
    road[a] += 1
    road[b] -= 1


k = road[0]
update = []  # дорога с жалобами

for i in range(1, len(road)):
    update.append(k)
    k += road[i]


count_road, len_roads = 0, 0

for i in range(1, len(update)):
    if update[i-1] == 0 and update[i] > 0:
        start = i

    if update[i-1] > 0 and update[i] == 0:
        count_road += 1
        len_roads += (i - start)

print(count_road, len_roads)
