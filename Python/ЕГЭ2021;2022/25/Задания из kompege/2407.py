
p=7*13*17*23*29
q=1

while p*q<1_000_000_000:
    q+=1

st=p*q
count=0
for i in range(st,2_000_000_001,p):
    k=i
    if all(i%x!=0 for x in [3,5]):
        a=set()
        for x in range(1,int(i**0.5)+1):
            if i%x==0:
                if x%2==1: a.add(x)
                if (i//x)%2==1: a.add(i//x)
                if len(a)>100:
                    count+=1
                    break

print(count)