
def f(a,c,m):
    if a>=40: return c%2==m%2
    if c==m: return 0

    h=[f(a+1,c+1,m),f(a+4,c+1,m),f(a*2,c+1,m)]

    return any(h) if (c+1)%2==m%2 else all(h)

t19=[]
t20=[]
t21=[]

t1=[]
for a in range(1,40):
    for m in range(1,5):
        if f(a,0,m)==1:
            if m==1: t1.append(a)
            if m==2: t19.append(a)
            if m==3 and a not in t1: t20.append(a)
            if m==4: t21.append(a)


print('19 - ',min(t19))
print('20 - ',t20[0],t20[1])
print('21 - ',min(t21))