def F(n):
    for i in range(len(n)-1):
        if (n[i]%2==n[i+1]%2): return False
    else: return True

a=[x for x in range(16)]
c=0
from itertools import *
for i in permutations(a,r=3):
    if (i[0]!=0) and (F(i)==True): c+=1

print(c)