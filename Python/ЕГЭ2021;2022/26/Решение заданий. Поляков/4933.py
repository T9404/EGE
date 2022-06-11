'''
Автомат фиксирует пассажиров некоторого автобуса по ходу рейса. У каждого пассажира 
фиксируется время входа и выхода с момента начала рейса. Необходимо узнать максимальное 
количество пассажиров, одновременно находящихся в автобусе, и общее время, когда в автобусе 
был хотя бы один пассажир. Временем входа и выхода в автобус пренебречь.
'''
# https://prnt.sc/w58GXpXbaATM


f = open('26.txt')
n = int(f.readline())


interval = [0] * 100000

# "100000" Взяли случайно. Если бы числа не хватило,
# то мы бы получили ошибку и увеличили его.


for _ in range(n):
    time_1, time_2 = map(int, f.readline().split())
    interval[time_1] += 1
    interval[time_2] -= 1


count, total_time, current = 0, 0, 0


for i in range(100000):
    current += interval[i]

    if current >= 1:
        total_time += 1

    count = max(current, count)


print(count, total_time)
