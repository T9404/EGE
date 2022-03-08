f = open('26-75.txt')
n = int(f.readline())


interval = [0]*100000

# "100000" Взяли случайно. Если бы числа не хватило,
# то мы бы получили ошибку и увеличили его.


for _ in range(n):
    time_1, time_2 = map(int, f.readline().split())
    interval[time_1] += 1
    interval[time_2] -= 1


count, total_time, curr = 0, 0, 0

for i in range(100000):
    curr += interval[i]

    if curr >= 1:
        total_time += 1

    count = max(curr, count)


print(count, total_time)
