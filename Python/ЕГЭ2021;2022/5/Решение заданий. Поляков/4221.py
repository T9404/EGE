m=float('inf')
for k in range(1,1000):
    i=k
    a=''
    while i:
        a+=str(i%4)
        i=i//4
    a=a[::-1]
    if (k%2==1):
        a='2'+a+'11'
    else: a='13'+a+'02'

    g=int(a,4)
    if (g>1000):
        m=min(m,g)

print(m)