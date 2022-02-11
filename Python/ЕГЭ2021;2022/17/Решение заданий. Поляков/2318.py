s,maxc=0,0
for i in range(2807,8559):
    if (i%9==5) and (i%2==1) and (i%4==3):
        s+=i
        maxc=max(maxc,i)
print(maxc,s)