def F(n):
    if n==1: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    else: return True

def G(n):
    a=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if F(i)==True: a.add(i)
            if F(n//i)==True: a.add(n//i)
    return sum(a)

for i in range(33333,55556):
    if (G(i)!=0) and (i%G(i)==0) and (G(i)>250):
        print(i,G(i))