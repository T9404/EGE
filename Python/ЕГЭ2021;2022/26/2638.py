f=open('data/26-k1.txt')
n, k =map(int, f.readline().split())
dt=[int(f.readline()) for _ in range(n)]
f.close()
dt.sort()
sale=[x*0.2 for x in dt[-k:]]
print(dt[len(dt)-1-k-1],int(sum(sale)))