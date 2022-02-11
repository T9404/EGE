from itertools import permutations
c=0
for i in range(700,801):
    a=[(str(i)[0]),(str(i)[1]),(str(i)[2])]
    maxc,minc=0,1000
    for k in permutations(a,2):
        if (k[0]!='0'):
            maxc=max(maxc,int(k[0]+k[1]))
            minc=min(minc,int(k[0]+k[1]))
    if (maxc-minc==80):
        c+=1

print(c)
