f = open('C:\\Users\\XiaoMai\\Downloads\\27-8a.txt')
n = int(f.readline())


a = [int(f.readline()) for _ in range(4)]


min_kvm, min_sum = float('inf'), float('inf')

for _ in range(5, n+1):
    x = int(f.readline())

    min_sum = min(min_sum, x**2+min_kv)

    min_kv = min(min_kv, x**2)

    min_kv = min(min_kv, a[0]**2)
    a.pop(0)
    a.append(x)

print(min_sum)
