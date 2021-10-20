f=open('C:\\Users\\XiaoMai\\Downloads\\27-B (2).txt')
n=int(f.readline())

a=[]
c=0
for _ in range(n):
    x=int(f.readline())
    ost=x%2
    q=[d for d in a if (d%2==(1-ost))] # d % 2 == (1 - ost)   -> только в этом случае сумма будет нечетна, если четна: != 
    if (len(q)!=0): # если массив не пустой
        min_q=min(q) # минимальный
        if (x>min_q): # правый элемент - х
            c+=len(q) # новые пары с х
    a.append(x)

print(c)



