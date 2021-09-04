#зАдАчА с открытого курса №1
#https://vk.com/ege_info_open?w=wall-205865487_471

#почитать: https://habr.com/ru/post/421071/

f = open('17.txt')
n = 5000
a = [int(f.readline()) for _ in range(n) ]
k, mak = 0, 0
for i in range(1, n):
    if (a[i-1] + a[i]) % 3 == 0:
        if (a[i-1]+a[i]) % 6 != 0:
            if abs(a[i]*a[i-1]) % 10 == 8:
                mak = max(mak, a[i-1]+a[i])
                k+=1
print(k, mak)

