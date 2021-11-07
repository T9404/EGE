c=0
for i in range(1,100000):
    if (i%2==0):
        i=i//2
    else: i-=1

    if (i%3==0):
        i=i//3
    else: i-=1

    if (i%7==0):
        i=i//7
    else: i-=1

    if (i==2):
        c+=1
print(c)
