# 1) Способ

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










# 2) Способ

f = open('C:\\Users\\XiaoMai\\Downloads\\26 (43).txt')
n = int(f.readline())


a = [0]*2_000_000


for _ in range(n):
    st, end = map(int, f.readline().split())
    for i in range(st, end):
        a[i] = 1


s = ''

for i in a:
    s += str(i)


s = s.replace('0', ' ', s.count('0')).split()


p = [len(x) for x in s]
print(len(p), sum(p))
