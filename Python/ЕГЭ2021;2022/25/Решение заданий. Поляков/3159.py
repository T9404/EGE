def F(n):
    pair=set()
    m=0
    c=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            pair.add((i,n//i))
    for x,y in pair:
        if abs(x-y)<=90:
            c+=1
            m=max(m,x,y)
    if c>=3:
        return m
    else: return 0

for i in range(500000,10**6+1):
    if F(i)!=0:
        print(i,F(i))

