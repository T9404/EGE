def F(n):
    for i in range(2,int(n**0.5)+1):
        if (n%i==0): return False
    else: return True

c1=[]
l1=10**7-1
while len(c1)<5:
    if (F(l1)==True): c1.append(l1)
    l1-=1

c2=[]
l2=10**7+1
while len(c2)<5:
    if (F(l2)==True): c2.append(l2)
    l2+=1

c1.sort()
c2.sort()
c=c1+c2
for i in c:
    print(abs(10**7-i),i)



