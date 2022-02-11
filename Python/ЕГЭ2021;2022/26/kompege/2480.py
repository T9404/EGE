f = open('C:\\Users\\XiaoMai\\Downloads\\26 (43).txt')
n = int(f.readline())

a = [0]*2_000_000

for _ in range(n):
    st, end = map(int, f.readline().split())
    for i in range(st, end):
        a[i] = 1

s = ''
for i in a:
    s += str(i)

s = s.replace('0', ' ', s.count('0')).split()
p = [len(x) for x in s]
print(len(p), sum(p))
