def F(n):
    razn=set()
    m=0
    for i in range(1,int(n**0.5)+1):
        if (n%i==0):
            if (abs(i-n//i)<=90):
                razn.add(abs(i-n//i))
                m=max(m,i,n//i)
    if (len(razn)>=3):
        return m
    else: return 0

for i in range(500000,1000001):
    if (F(i)!=0):
        print(i,F(i))
