def F(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    else: return True

a=[]
c1=0
for i in range(10**7-1,0,-1):
    if F(i)==True:
        c1+=1
        if c1<=3: a.append([i,10**7-i])
        else: break
c2=0
for i in range(10**7-1,10**8):
    if F(i)==True:
        c2+=1
        if c2<=3: a.append([i,i-10**7])
        else: break

a.sort()
for x,y in a:
    print(y,x)