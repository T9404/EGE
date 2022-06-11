'''
На производстве станок с ЧПУ обрабатывал некоторый набор деталей. В каждый момент времени станок 
может обрабатывать только одну деталь. Каждая деталь изготавливалась в определённый промежуток 
времени с момента начала рабочего дня. Простоем считается временной участок длиной не менее M секунд, 
в которые не обрабатывается ни одна деталь. Инженер решил узнать, какое количество простоев произошло 
за день и какова длительность наибольшего простоя. Общая длительность рабочего дня L секунд.
'''
# https://prnt.sc/FzciSo26Gn4h


f = open('26.txt')
l, m, n = map(int, f.readline().split())


timetable = [0] * l

for _ in range(n):
    a, b = map(int, f.readline().split())
    timetable[a] += 1
    timetable[a + b] -= 1


ans_count, ans_max, start = 0, 0, False
elem = timetable[0]


for i in range(1, len(timetable)):
    last_k = elem
    elem += timetable[i]

    if (elem == 0) and (start == False):
        start = i

    if (elem == 1 and last_k == 0) or (i == len(timetable) - 1):
        if (i - start + 1) >= m:
            ans_count += 1
            ans_max = max(i-start+1, ans_max)
        start = False


print(ans_count, ans_max)
