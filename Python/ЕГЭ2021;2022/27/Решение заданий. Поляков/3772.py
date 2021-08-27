#(№ 3772) В файле записана последовательность натуральных чисел.
#Гарантируется, что все числа различны.
#Из этой последовательности нужно выбрать три числа, чтобы их сумма делилась на 3 и была наименьшей.
#Какую наименьшую сумму можно при этом получить?

f=open('C:\\Users\\XiaoMai\\Downloads\\27-53b.txt')
n=int(f.readline())

d1=[float('inf')]*3
d2=[float('inf')]*3
min_sum=float('inf')

for _ in range(n):
    x=int(f.readline())

    for i in range(3):
        if ((d2[i]+x)%3==0):
            min_sum=min(min_sum,d2[i]+x)
    for i in range(3): d2[(i+x)%3]=min(d2[(i+x)%3],d1[i]+x)

    d1[x%3]=min(d1[x%3],x)

print(min_sum)