from math import ceil


f = open('data/26-s1.txt')
n = int(f.readline())


coins = []

for i in range(n):
    coins += [int(f.readline())]


notsale = [x for x in coins if x <= 100]

for c in notsale:
    del coins[coins.index(c)]

coins.sort()


sale = [coins[:len(coins)//2:]]
max_sale = max(sale)

notsale += coins[len(coins)//2::]


for i in range(len(sale)):
    sale[i] = sale[i]*0.9

print(ceil(sum(sale)+sum(notsale)), max_sale)
