def F(n):
    d=10
    for i in range(len(n)-1):
        if (n[i]+10!=n[i+1]):
            return False
            break
    else: return True

for i in range(854321,1087655):
    s=set()
    for k in range(2,int(i**0.5)+1):
        if (i%k==0):
            s.add(k)
            s.add(i//k)
    if (len(s)>1) and (F(sorted(s))==True): print(i,min(s))
