def F(n):
    if n==1: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    else: return True

c=0
for i in range(2532000,2532161):
    if F(i)==True:
        c+=1
        if c%3==1: print(c,i)
