f = open('26-j4.txt')
n = int(f.readline())

a = sorted([int(f.readline()) for x in range(n)])

little = a[:len(a)//10]
big = a[(len(a)//10)*9:]

mak = a[(len(a)//10)*9-1]

print(sum(a)-sum(little)-sum(big), mak)
