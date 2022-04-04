def f(a,b,c,m):
    if a+b>=45: return c%2==m%2
    if c==m: return 0

    h=[f(a+2,b,c+1,m),f(a,b+2,c+1,m),f(a*3,b,c+1,m),f(a,b*3,c+1,m)]

    return any(h) if (c+1)%2==m%2 else all(h)

t19=[]
t20=[]
t21=[]

t1=[]
t2=[]
for a in range(1,44):
    for b in range(1,44):
        for m in range(1,6):
            if (a+b<=43) and (f(a,b,0,m)==1):
                if m==2: t19.append(1)

for b in range(1,44):
    for m in range(1,6):
        if (4+b<=43) and (f(4,b,0,m)==1):
            if m==1: t1.append(b)
            if m==3 and not b in t1: t20.append(b)

for b in range(1,44):
    for m in range(1,6):
        if (13+b<=43) and (f(13,b,0,m)==1):
            if m==2: t2.append(b)
            if m==4 and not b in t2: t21.append(b)

print('19 - ',len(t19))
print('20 - ',min(t20),max(t20))
print('21 - ',t21[0])