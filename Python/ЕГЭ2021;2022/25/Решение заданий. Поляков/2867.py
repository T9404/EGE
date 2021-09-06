#(№ 2867) (Д.Ф. Муфаззалов) Число называется полусовершенным, если сумма всех или некоторых его собственных делителей
#(то есть всех положительных делителей, отличных от самого́ числа) совпадает с самим этим числом.
#Определите количество таких чисел в диапазоне [300; 350] и наибольшее из них.

from itertools import *
c=0
maxc=0
for i in range(300,351):
    a=set()
    a.add(1)
    w=0
    for k in range(2,int(i**0.5)+1):
        if (i%k==0):
            a.add(k)
            a.add(i//k)
    if (sum(a)>=i):
        for k in range(2,len(a)-1):
           for q in combinations(a,r=k):
               if (sum(a)-sum(q)==i): w+=1
    if (w>0):
        c+=1
        maxc=max(maxc,i)

print(c,maxc)