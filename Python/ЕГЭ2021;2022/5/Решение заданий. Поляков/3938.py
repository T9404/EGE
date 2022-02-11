c=0
for i in range(1,10000):
    a=bin(i)[2:]
    k=a+str(a.count('1')%2)
    if (a.count('1')>a.count('0')):
        k+='0'
    else: k+='1'

    if (50<=int(k,2)<=80):
        c+=1

print(c)

