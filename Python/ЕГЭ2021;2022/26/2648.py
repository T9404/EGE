from math import ceil
coins = []
f=open('data/26-s1.txt')
n = int(f.readline())
for i in range(n):
    coins+=[int(f.readline())]

f.close()
notsale = [x for x in coins if x<=100]

for c in notsale:
    del coins[coins.index(c)]

coins=sorted(coins)
sale=[]
sale+=coins[:len(coins)//2:]
maxsale =max(sale)
notsale+=coins[len(coins)//2::]

for i in range(len(sale)):
    sale[i]=sale[i]*0.9

print(ceil(sum(sale)+sum(notsale)), maxsale)