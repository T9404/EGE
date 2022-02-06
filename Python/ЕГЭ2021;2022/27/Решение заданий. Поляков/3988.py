f = open('файлик')
n = int(f.readline())


sumax, sumin = 0, 0 

# в подходящих парах(второе число нечетное) сумма мин пары, в которой 1 число (МАКСИМУМ) - четное 2(МИНМУМ) число- четное
s1 = s2 = s3 = s4 = float('inf')

for _ in range(n):
    a = [int(x) for x in f.readline().split()]

    if (a[1] % 2 == 1):
        sumax += max(a)  # добавили максимальное число
        sumin += min(a)  # добавили минимальное

        if (max(a) % 2 == 0) and (min(a) % 2 == 0):
            ''' тут мы ищем минимальную суммы группы, которую мы уберем '''
            s1 = min(sum(a), s1)

        if (max(a) % 2 == 1) and (min(a) % 2 == 1):
            s2 = min(sum(a), s2)

        if (max(a) % 2 == 0) and (min(a) % 2 == 1):
            s3 = min(sum(a), s3)

        if (max(a) % 2 == 1) and (min(a) % 2 == 0):
            s4 = min(sum(a), s4)



# сначала мы просто нашли суммы макс и мин групп, а затем, в зависимости от четности вычитаем группы
# четное-четное=четное
# четное-нечетное=нечетное
# нечетное-четное=нечетное
# нечетное-нечетное=четное


if (sumax % 2 == 0) and (sumin % 2 == 1):
    print(sumax+sumin)

if (sumax % 2 == 0) and (sumin % 2 == 0):
    print(sumax+sumin-s3)

if (sumax % 2 == 1) and (sumin % 2 == 1):
    print(sumax+sumin-s4)
    
if (sumax % 2 == 1) and (sumin % 2 == 0):
    print(sumax+sumin-s2)
