from functools import lru_cache

@lru_cache(None)
def f(x,y,z,c,m):
    if (x+y+z)>=71: return c%2==m%2
    if c == m: return 0

    h=[f(x+3,y,z,c+1,m),f(x,y+3,z,c+1,m),f(x,y,z+3,c+1,m),f(x*2,y,z,c+1,m),f(x,y*2,z,c+1,m),f(x,y,z*2,c+1,m)]

    return any(h) if (c+1)%2==m%2 else all(h)

t20=[]
t21=[]
t1=[]
t2=[]

for s in range(1,59):
    for m in range(1,7):
        if f(s,5,7,0,m)==1:
            if m==2: t2.append(s)
            if m==1: t1.append(s)
            if m==3 and not s in t1: t20.append(s)
            if m==4 and not s in t2: t21.append(s)

print('19 - ',15) # all -> any m==2
print('20 - ',min(t20),max(t20))
print('21 - ',t21[0])

