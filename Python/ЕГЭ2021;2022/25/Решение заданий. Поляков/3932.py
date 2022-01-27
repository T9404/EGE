def F(n):
    a=set()
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            a.add(i)
            a.add(n//i)
    return len(a)

for i in range(700000+1,10**8):
    if F(i)<F(i+1)<F(i+2)<F(i+3)<F(i+4):
        c=i
        while c<i+5:
            print(c,F(c))
            c+=1
        break