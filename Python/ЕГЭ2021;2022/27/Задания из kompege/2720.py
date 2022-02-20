# 1 Решение

f = open('27B.txt')
n = int(f.readline())


chet_7 = 0

for _ in range(n):
    x = int(f.readline())

    if x % 7 == 0:
        chet_7 += 1


nechet_7 = n - chet_7

print((nechet_7*chet_7) + (chet_7*(chet_7-1)//2))





# 2 Решение

f = open('27B.txt')
n = int(f.readline())


answer, count_7 = 0, 0

for i in range(n):
    x = int(f.readline())

    if x % 7 == 0:
        count_7 += 1
        answer += i  # Важно, индексация начинается с 0
    else:
        answer += count_7

print(answer)
