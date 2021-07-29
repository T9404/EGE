#(№ 2679) (А. Жуков) Имеется набор данных, состоящий из целых чисел.
#Необходимо определить максимальное произведение подпоследовательности, состоящей из одного или более идущих подряд элементов.
f=open('C:\\Users\\XiaoMai\\Downloads\\27-19b.txt')
n=int(f.readline())

s=[1]
max_pr=0

for i in range(n):
    x=int(f.readline())
    s=[a*x for a in s]+[x]
    for a in s:
        if (a==0):
            s.remove(0)
        max_pr=max(max_pr,a)

print(max_pr)
