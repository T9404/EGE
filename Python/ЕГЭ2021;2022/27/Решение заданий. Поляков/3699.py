# 3699 Набор данных состоит из нечётного количества пар натуральных чисел.
#Необходимо выбрать из каждой пары ровно одно число так,
#чтобы сумма выбранных чисел была максимальной при условии, что чётность этой суммы совпадает с чётностью большинства выбранных чисел.
#Определите максимальную сумму, которую можно получить при таком условии. Гарантируется, что удовлетворяющий условиям выбор возможен.


f=open('_')
n=int(f.readline())

max_sum=0
min_raznica=float('inf')

cet=0
necet=0

cet1=0
necet1=0
for _ in range(n):
    a=[int(x) for x in f.readline().split()]
    max_sum+=max(a)
    if (max(a)%2==0):
        cet+=1
    else:
        necet+=1
    if ((a[0]%2)!=(a[1]%2)) and (abs(a[0]-a[1])<min_raznica):
        min_raznica=abs(a[0]-a[1])
        if (min(a)%2==0):
            cet1=1
            necet1=0
        else:
            cet1 = 0
            necet1 = 1


if (cet>necet) and (max_sum % 2 ==1) and (cet+cet1>necet+necet1): print(max_sum-min_raznica)
if (cet<necet) and (max_sum % 2 ==0) and (cet+cet1<necet+necet1): print(max_sum-min_raznica)


