f = open('2650.txt')
l, m, n = map(int, f.readline().split())

timetable = [0]*l

for _ in range(n):
    a, b = map(int, f.readline().split())
    timetable[a] += 1
    timetable[a+b] -= 1


ans_count, ans_max, start = 0, 0, False
k = timetable[0]

for i in range(1, len(timetable)):
    last_k = k 
    k += timetable[i]

    if (k == 0) and (start == False):
        start = i
    
    if (k == 1 and last_k == 0) or (i == len(timetable) - 1):
        if (i - start + 1) >= m:
            ans_count += 1
            ans_max = max(i-start+1, ans_max)
        start = False


print(ans_count, ans_max)