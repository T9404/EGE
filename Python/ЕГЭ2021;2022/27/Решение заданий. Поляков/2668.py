#(№ 2668) Имеется набор данных, состоящий из положительных целых чисел, каждое из которых не превышает 1000.
#Они представляют собой результаты измерений, выполняемых прибором с интервалом 1 минута.
#Требуется найти для этой последовательности контрольное значение –
#наименьшую сумму квадратов двух результатов измерений, выполненных с интервалом не менее, чем в 5 минут.

f=open('C:\\Users\\XiaoMai\\Downloads\\27-8a.txt')
n=int(f.readline())

a=[int(f.readline()) for _ in range(4)]

min_kv=float('inf')
min_sum=float('inf')

for _ in range(5,n+1):
    x=int(f.readline())

    min_sum=min(min_sum,x**2+min_kv)

    min_kv=min(min_kv,x**2)

    min_kv=min(min_kv,a[0]**2)
    a.pop(0)
    a.append(x)

print(min_sum)