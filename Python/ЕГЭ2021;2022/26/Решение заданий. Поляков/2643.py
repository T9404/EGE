f = open('26-j1.txt')
n = int(f.readline())


a = [0]*100

for _ in range(n):
    a[int(f.readline())] += 1


count = a[50]//2

for i in range(1, 50):
    count += min(a[i], a[100-i])

print(count)
