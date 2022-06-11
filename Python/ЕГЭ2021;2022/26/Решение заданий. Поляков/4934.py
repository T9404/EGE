'''
На производстве станок с ЧПУ обрабатывал некоторый набор деталей. В каждый момент времени 
станок может обрабатывать только одну деталь. Каждая деталь изготавливалась в определённый 
промежуток времени с момента начала рабочего дня. Простоем считается временной участок длиной 
не менее M секунд, в течение которого не обрабатывается ни одна деталь. Инженер решил узнать, 
какое количество простоев произошло за день и какова длительность наибольшего простоя. Общая 
длительность рабочего дня L секунд.
'''
# https://prnt.sc/4OYn_ii2fmWl


f = open('26.txt')
l, m, n = map(int, f.readline().split())


timetable = []


for _ in range(n):
    time = list(map(int, f.readline().split()))
    timetable.append(time)


# начало нового промежутка
timetable.sort(key=lambda x: x[0])


count, best = 0, 0


for i in range(len(timetable) - 1):
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
