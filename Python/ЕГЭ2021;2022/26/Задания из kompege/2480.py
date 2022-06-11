'''
На сайте министерства транспорта организовали приём жалоб автомобилистов на плохое качество дорог. 
К моменту, когда министерство выделило средства на ремонт одной из автомагистралей, на сайте 
накопилось уже некоторое количество жалоб. Каждая жалоба описывает начало и конец проблемного 
участка (примерное расстояние от начала автомагистрали в метрах). Так как жалобы писались независимо 
друг от друга разными людьми, некоторые описываемые участки автомагистрали накладываются друг на друга. 
Для планирования необходимых ремонтных ресурсов министерство решило узнать, сколько заявлено непрерывных 
участков дороги и какова их общая длина.
'''
# https://prnt.sc/P2v_13l1IhSq


# (I) Способ

f = open('2480.txt')
n = int(f.readline())


# из условия меньше 2_000_000
road = [0]*2_000_001


for _ in range(n):
    road, b = map(int, f.readline().split())
    road[road] += 1
    road[b] -= 1


k = road[0]
# дорога с жалобами
alert = []

for i in range(1, len(road)):
    alert.append(k)
    k += road[i]


count_road, len_roads = 0, 0


for i in range(1, len(alert)):
    if alert[i-1] == 0 and alert[i] > 0:
        start = i

    if alert[i-1] > 0 and alert[i] == 0:
        count_road += 1
        len_roads += (i - start)


print(count_road, len_roads)




# (II) Способ

f = open('26.txt')
n = int(f.readline())


road = [0] * 2_000_000


for _ in range(n):
    start, end = map(int, f.readline().split())
    for i in range(start, end):
        road[i] = 1


line = ''
for i in road:
    line += str(i)


line = line.replace('0', ' ', line.count('0')).split()


p = [len(x) for x in line]
print(len(p), sum(p))
