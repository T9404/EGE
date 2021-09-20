f=open('data/26-k2.txt')
n, k =map(int, f.readline().split())
dt=[int(f.readline()) for _ in range(n)]
f.close()
dt.sort()
true_data=dt[k-1:-k]
print(max(true_data),sum(true_data)//len(true_data))