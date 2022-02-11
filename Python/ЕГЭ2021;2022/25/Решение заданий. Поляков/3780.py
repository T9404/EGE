def F(n):
    if n==1: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    else: return True

for i in range(63_000_000,75_000_001):
    c=i
    while c%2==0:
        c=c//2
    if F(int(c**0.25))==True and int(c**0.25)**4==c:
        c=int(c**0.25)
        print(i,c**4)