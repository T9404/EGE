def F(n):
    razn=set()
    for i in range(2,int(n**0.5)+1):
        if (n%i==0):
            razn.add(abs(i-n//i))
    if (len(razn)>=2) and (min(list(razn))>4444) and (max(list(razn))%min(list(razn))==0):
        return min(x for x in razn if (x!=0))
    else: return 0

for i in range(543210,987655):
    if (F(i)!=0):
        print(i,F(i))