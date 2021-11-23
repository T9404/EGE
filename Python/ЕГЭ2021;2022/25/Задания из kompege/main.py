def F(n):
    a=set()
    for i in range(2,int(n**0.5)+1):
        if (n%i==0): a.add(i); a.add(n//i)
    if (len(a)>=5):
        a=list(a)
        a.sort()
        if (0<(a[0]*a[1]*a[2]*a[3]*a[4])<n):
            return a[0]*a[1]*a[2]*a[3]*a[4]
        else: return 0
    else: return 0

c=0
for i in range(200000001,100000000000,1):
    if (F(i)!=0):
        c+=1
        if (c<=5):
            print(F(i))
        else: break