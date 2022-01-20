def F(x,a1,a2):
    return (37<=x<=60) <= (((40<=x<=77) and ((not(a1<=x<=a2)))) <= (not(37<=x<=60)))

m=10000
for a1 in range(100):
    for a2 in range(a1+1,100):
        if all(F(x,a1,a2)==1 for x in range(100)):
            m=min(m,a2-a1)

print(m)