f = open('26-76.txt')
l, m, n = map(int, f.readline().split())


timetable = []

for _ in range(n):
    time = list(map(int, f.readline().split()))
    timetable.append(time)

timetable.sort(key=lambda x: x[0])  # начало нового промежутка


count, best = 0, 0

for i in range(len(timetable)-1):
    nothing = timetable[i+1][0] - timetable[i][1]
    if nothing >= m:
        count += 1
        best = max(nothing, best)


# Обработка концов

if timetable[0][0] >= m:
    count += 1
    best = max(timetable[0][0], best)


if l - timetable[-1][1] >= m:
    count += 1
    best = max(l - timetable[-1][1], best)


print(count, best)
